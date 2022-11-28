import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        GameService gameService = new GameService();
        gameService.initialise();
        Scanner sc = new Scanner(System.in);
        System.out.println("\n0 - UP");
        System.out.println("1 - RIGHT");
        System.out.println("2 - BOTTOM");
        System.out.println("3 - LEFT");
        while (gameService.getCurrentState() == State.ONGOING) {
            int move = sc.nextInt();
            if (move < 0 || move > 3) {
                System.out.println("Please enter a valid move");
                continue;
            }
            Direction directionToMove = Direction.values()[move];
            gameService.move(directionToMove);
        }
        System.out.println(gameService.getCurrentState());
    }
}