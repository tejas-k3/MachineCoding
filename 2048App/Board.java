import java.util.List;
import java.util.ArrayList;

public class Board {
    public static class Cell {
        private final int row;
        private final int column;

        public Cell(int row, int column) {
            this.row = row;
            this.column = column;
        }

        public int getRow() {
            return row;
        }

        public int getColumn() {
            return column;
        }
    }

    public int getSize() {
        return size;
    }

    private final int size;
    private List<List<Integer>> grid;

    public Board(int size) {
        this.size = size;
        grid = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            grid.add(new ArrayList<>(size));
            for (int j = 0; j < size; j++) {
                grid.get(i).add(0);
            }
        }
    }

    public void setCell(Cell cell, int num) {
        int row = cell.getRow();
        int column = cell.getColumn();
        if (row < 0 || column < 0 || row >= size || column >= size) {
            throw new RuntimeException("Invalid cell passed");
        }
        this.grid.get(cell.getRow()).set(cell.getColumn(), num);
    }

    public boolean isCellVacant(Cell cell) {
        return grid.get(cell.row).get(cell.column) == 0;
    }

    public boolean contains(int num) {
        for (List<Integer> row : grid) {
            for (Integer cellValue : row) {
                if (cellValue == num) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean isFull() {
        for (List<Integer> row : grid) {
            for (Integer cellValue : row) {
                if (cellValue == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public void slideUp() {
        transpose();
        slideLeft();
        transpose();
    }

    public void slideDown() {
        transpose();
        slideRight();
        transpose();
    }

    public void slideRight() {
        reverse();
        slideLeft();
        reverse();
    }

    public void slideLeft() {
        for (int i = 0; i < size; i++) {
            grid.set(i, slideRowLeft(grid.get(i)));
        }
    }

    private List<Integer> slideRowLeft(List<Integer> row) {
        List<Integer> updatedRow = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            updatedRow.add(0);
        }
        int i = 0;
        int j = 0;
        while (i < size) {
            if (row.get(i) == 0) {
                i++;
            } else if (row.get(i) != 0 && updatedRow.get(j) == 0) {
                updatedRow.set(j, row.get(i));
                i++;
            } else if (row.get(i) == updatedRow.get(j)) {
                updatedRow.set(j, updatedRow.get(j) + row.get(i));
                i++;
                j++;
            } else {
                j++;
            }
        }
        return updatedRow;
    }

    private void transpose() {
        List<List<Integer>> transpose = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            List<Integer> col = new ArrayList<>();
            for (List<Integer> row : grid) {
                col.add(row.get(i));
            }
            transpose.add(col);
        }
        grid = transpose;
    }

    private void reverse() {
        for (int i = 0; i < size; i++) {
            reverseRow(grid.get(i));
        }
    }

    private void reverseRow(List<Integer> row) {
        int i = 0, j = size - 1;
        while (i < j) {
            int temp = row.get(i);
            row.set(i, row.get(j));
            row.set(j, temp);
            i++;
            j--;
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (List<Integer> row : grid) {
            for (Integer cellValue : row) {
                sb.append(cellValue == 0 ? "-" : cellValue.toString());
                sb.append(" ");
            }
            sb.append("\n");
        }
        return sb.toString();
    }
}
