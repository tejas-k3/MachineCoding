import java.util.Random;

public class GameService {
    private final Board board;

    private static final int DEFAULT_GRID_SIZE = 4;

    public GameService(int gridSize) {
        this.board = new Board(gridSize);
    }

    public GameService() {
        this(GameService.DEFAULT_GRID_SIZE);
    }

    public void initialise() {

        Board.Cell randomCell1 = getRandomCell();
        Board.Cell randomCell2 = getRandomCell();

        while (randomCell2.getRow() == randomCell1.getRow() && randomCell2.getColumn() == randomCell1.getColumn()) {
            randomCell2 = getRandomCell();
        }

        board.setCell(randomCell1, 2);
        board.setCell(randomCell2, 2);

        System.out.println(board);
    }

    public State getCurrentState() {
        if (board.contains(2048)) {
            return State.VICTORY;
        } else if (board.isFull()) {
            return State.OVER;
        } else {
            return State.ONGOING;
        }
    }

    public void move(Direction directionToMove) {
        switch (directionToMove) {
            case UP:
                board.slideUp();
                break;
            case LEFT:
                board.slideLeft();
                break;
            case RIGHT:
                board.slideRight();
                break;
            case BOTTOM:
                board.slideDown();
                break;
        }
        Board.Cell randomCell = getRandomCell();
        while (!board.isCellVacant(randomCell)) {
            randomCell = getRandomCell();
        }
        board.setCell(randomCell, 2);
        System.out.println(board);
    }

    private Board.Cell getRandomCell() {
        Random random = new Random();
        return new Board.Cell(random.nextInt(board.getSize()), random.nextInt(board.getSize()));
    }
}