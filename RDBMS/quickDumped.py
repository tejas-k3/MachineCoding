# Ref https://medium.com/@tg6897/design-in-memory-db-with-indexing-52d33adceb91
class ColumnDataType:
    """
    Base class wrapper over primitive data types
    """

    def __init__(self, data_type):
        self.data_type = data_type

    def validate(self, val):
        if not isinstance(self.data_type, val):
            raise Exception("Invalid_data_point_type")
        return val


class IntDataType(ColumnDataType):
    """
    IntData type class provides validations over integer like, min and max values allowed
    """

    def __init__(self, _min_value, _max_value):
        self.min_value = _min_value
        self.max_value = _max_value
        super(IntDataType, self).__init__(int)

    def validate(self, val):
        """
        validate min and max values
        """
        super(IntDataType, self).validate(val)
        if not self.min_value <= val <= self.max_value:
            raise OutOfRangeException("int_out_of_range")
        return val


class StrDataType(ColumnDataType):
    
    def __init__(self, _min_value, _max_value):
        self.min_value = _min_value
        self.max_value = _max_value
        super(StrDataType, self).__init__(str)

    def validate(self, val):
        """
        validate max len of the string
        """
        super(StrDataType, self).validate(val)
        if not self.min_value <= len(val) <= self.max_value:
            raise OutOfRangeException("string_len_out_of_range")
        return val

class SchemaMember:
    """
    This class provides the actual column to be used in schema
    It uses ColumnDataType class to enforce type
    """

    def __init__(self, column_name, column_type, required=True, allow_none=False):
        """
        column_name : Name of the column
        column_type: Instance of ColumnDataType class ie. can be IntDataType, StrDataType etc.
        required: Is the column value required in data or not
        allow_none: Is the column value allowed as null or not
        """
        self.column_name = column_name
        self.column_type = column_type
        self.required = required
        self.allow_none = allow_none

    def validate_value(self, val):
        """
        validates column value
        """
        if val is None and not self.allow_none:
            raise InvalidValueException(f"None_not_allowed_in_{self.column_name}")
        return self.column_type.validate(val)

from sortedcontainers import SortedDict


class Index:
    """
    Base class for Index
    Provides Interface for indexing/querying and removing indexes
    For now index storage is considered as a SortedDict(equivalent to balanced BST) but we can abstract this as well
    and make a generic storage interface , so that we can plugin different storages without ever changing indexing code.
    """

    def __init__(self, index_name, primary_key):
        """
        index_name : Name of the index , normally column_name
        primary_key: Primary key of the DB, this acts as a query result, ie. provides primary key of data which satisfies
        filter conditions.(we can remove it and take primary key while filtering as well)
        index_storage: Storage for indexes. can abstract the same into interface
        """
        self.index_name = index_name
        self.primary_key = primary_key
        self.index_storage = SortedDict()

    def index_row_data(self, row_data):
        """
        indexes the row data.
        we remove older index first so that we don't get wrong results
        """
        self.remove_indexed_val(row_data)
        self.index_data(row_data)

    def index_data(self, row_data):
        """
        does indexing of the data in index storage
        """
        raise Exception("No_default_implementation")

    def get_data(self, filter_val):
        """
        return values satisfying the condition, override as required
        """
        return self.index_storage.get(filter_val, set())

    def remove_indexed_val(self, row_data):
        """
        removes indexes
        """
        raise Exception("No_default_implementation")

class ReverseIndex(Index):
    """
    Basic Reverse index implementation. Just storing val<>key mapping
    """

    def index_data(self, row_data):
        """
        Indexes the val in index storage, basically val<>primary_key mapping
        """
        if not self.index_storage.get(row_data[self.index_name]):
            self.index_storage[row_data[self.index_name]] = set()
        self.index_storage[row_data[self.index_name]].add(row_data[self.primary_key])

    def remove_indexed_val(self, row_data):
        """
        Remove the indexed value
        """
        if row_data[self.primary_key] in self.index_storage:
            self.index_storage[row_data[self.index_name]].remove(row_data[self.primary_key])


class FuzzyIndex(Index):
    """
    Fuzzy indexes: Instead of directly storing a val<>key mapping , here we will tokenize the value and store primary
    key in each one of them.
    very basic implementation of fuzzy index
    """

    def __init__(self, index_name, primary_key, seperator=" "):
        """
        seperator: used to tokenize the value, default is space (" ")
        """
        super(FuzzyIndex, self).__init__(index_name, primary_key)
        self.seperator = seperator

    def get_fuzzy_values(self, row_data):
        """
        returns values after tokenization
        """
        _val_to_index = row_data[self.index_name]
        fuzzy_values = _val_to_index.split(self.seperator)
        return fuzzy_values

    def index_data(self, row_data):
        """
        Index each of the fuzzy values, currently case sensitive
        """
        for _val in self.get_fuzzy_values(row_data):
            if not self.index_storage.get(_val):
                self.index_storage[_val] = set()
            self.index_storage[_val].add(row_data[self.primary_key])

    def remove_indexed_val(self, row_data):
        """
        Removes each of the fuzzy indexed value
        """
        for _val in self.get_fuzzy_values(row_data):
            if _val not in self.index_storage:
                continue
            key_to_remove = row_data[self.primary_key]
            if key_to_remove not in self.index_storage[_val]:
                continue
            self.index_storage[_val].remove(key_to_remove)

class Table:

    def __init__(self, table_name, table_schema, primary_key):
        """
        Table Name : name of the table
        table_schema: Instance of TableSchemaClass
        indexes: Instances of IndexClass
        primary_key: Primary key of the table
        table_data: Storage for table [Can abstract it into an interface , in order to use any storage as plugin]
        """
        self.table_name = table_name
        self.table_schema = table_schema
        self.indexes = {}
        self.primary_key = primary_key
        self.table_data = {}

    def create_index(self, column_name, index_type):
        """
        Creates a new index by providing column and index type
        """
        if column_name in self.indexes:
            raise Exception(f"Index_already_exists_{column_name}")
        self.indexes[column_name] = IndexType[index_type].value(column_name, self.primary_key)

    def insert_data(self, row_data):
        """
        Insert data into table , steps:
        1. Verify data using TableSchema
        2. If verified, push data into table
        3. Index additional data if defined in indexes
        """
        self.table_schema.validate_row_data(row_data)
        self.table_data[row_data[self.primary_key]] = row_data
        self.index_row_data(row_data)

    def index_row_data(self, row_data):
        """
        Indexes the row data using IndexClass instance
        """
        for _index in self.indexes:
            if _index in row_data:
                self.indexes[_index].index_row_data(row_data)

    def delete_data(self, key):
        """
        Delete data from the table and removes any index as well
        """
        if key not in self.table_data:
            raise Exception(f"Record_not_present_with_key_{self.primary_key}")
        _data = self.table_data[key]
        del self.table_data[key]
        for _index in self.indexes:
            if _index in _data:
                self.indexes[_index].remove_indexed_val(_data)

    def scan_table(self, filters, data):
        """
        Scan complete data on the filters defined.
        """
        if not filters:
            return data
        filtered_data = []
        for row in data:
            valid_data = True
            for filter_key in filters:
                if not (filters[filter_key] == row[filter_key]):
                    valid_data = False
                if valid_data:
                    filtered_data.append(row)
        return filtered_data

    def filter_on_indexes(self, filters, indexes):
        """
        Filters data on the indexes.
        It only works as a "AND" filter. So we query all indexes and send back primary keys which satisfies all indexes
        """
        _filtered_data = None
        for _filter_key in indexes:
            if _filtered_data is None:
                _filtered_data = self.indexes[_filter_key].get_data(filters[_filter_key])
                continue
            _filtered_data &= self.indexes[_filter_key].get_data(filters[_filter_key])
        return _filtered_data

    def filter_data(self, filters):
        """
        Filter data on the provided filters.(only uses AND)
        This is a simple implementation as follows:
        1. Check if the column on which filter is needed has an index. if yes then query that first.
        2. After all columns with indexes have been queried , filter the resultant data set on non-indexed
            columns. [This is done as querying indexes is fast , and our non indexed scan can work on a smaller data 
            set which we get from after querying on indexed columns]
        3. Combine result and return.
        """
        if self.primary_key in filters:
            if filters.get(self.primary_key) in self.table_data:
                return [self.table_data[filters.get(self.primary_key)]]
            return []
        _has_indexes = [_filter_key for _filter_key in filters if (_filter_key in self.indexes)]
        _no_indexes = [_filter_key for _filter_key in filters if (_filter_key not in self.indexes)]
        _filtered_data = self.filter_on_indexes(filters, _has_indexes)
        indexed_filtered_data = []
        if _filtered_data:
            indexed_filtered_data = [self.table_data[key] for key in _filtered_data]
        final_data = self.scan_table({k: filters[k] for k in _no_indexes},
                                     indexed_filtered_data if _has_indexes else self.table_data.values())
        return final_data


def table_flow(cls):
    # create schema
    user_schema = TableSchema()
    user_schema.add_schema_member(SchemaMember("user_id", StrDataType(0, 10), required=True))
    user_schema.add_schema_member(SchemaMember("user_name", StrDataType(0, 50)))
    user_schema.add_schema_member(SchemaMember("user_age", IntDataType(0, 100), required=False))

    # Create Table
    user_table = Table(table_name="users", table_schema=user_schema, primary_key="user_id")

    # create index
    user_table.create_index("user_name", "FUZZY")

    # insert seed data
    user_table.insert_data({"user_id": "user1", "user_name": "new user", "user_age": 20})
    user_table.insert_data({"user_id": "user2", "user_name": "improved user"})
    user_table.insert_data({"user_id": "user3", "user_name": "diff guy", "user_age": 30})

    print(user_table.filter_data({"user_name": "user"}))
    # out : [{'user_id': 'user1', 'user_name': 'new user', 'user_age': 20},
    # {'user_id': 'user2', 'user_name': 'improved user'}]

    print(user_table.filter_data({"user_name": "user", "user_age": 20}))
    # out : [{'user_id': 'user1', 'user_name': 'new user', 'user_age': 20}]

    user_table.delete_data("user2")
    print(user_table.filter_data({"user_name": "user"}))
    # out : [{'user_id': 'user1', 'user_name': 'new user', 'user_age': 20}]
