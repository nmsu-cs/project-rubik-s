// CubeSolver.java
// Class used to solve the Rubik's cube
// Copy of an old Solver.py but in java

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;



public class CubeSolver{

	public static String solve(int[] upper, int[] down, int[] front, int[]back, int[] left, int[] right){
		int[] cube = concatenateArrays(upper, down, front, back, left,right);

		String solvePath = solveTree(cube);
		return(solvePath);
	}

	// Function: solveTree
	// Purpose: Will iterate through a movement tree checking for solutions
	public static String solveTree(int[] cube){
		// Create Double ended queue
		Queue<StatePathPair> queue = new ArrayDeque<>();
		queue.offer(new StatePathPair(cube, ""));

		// Create set for already visited states, avoid creating duplicate subnodes
		Set<String> visited = new HashSet<>();

		// Set previousMove to Nothing
		String previousMove = "";

		// Level traverse the tree
		while(!queue.isEmpty()){
			// Pull StatePathPair object from queue
			StatePathPair statePathPair = queue.poll();
			int[] currentCube = statePathPair.getCube();
			String path = statePathPair.getPath();

			// Check if solved
			if(checkSolved(currentCube)){
				return(path);
			}

			// Add state to set
			String state = arrayToString(currentCube);
			if(visited.contains(state)){
				continue;
			}
			visited.add(state);

			// Interface for movement functions
			Movement[] moveFunctions = {
				new Movement(CubeSolver::moveUpperCW,  "U"),
				new Movement(CubeSolver::moveUpperCCW, "V"),
				new Movement(CubeSolver::moveUpper2,  "UU"),
				new Movement(CubeSolver::moveFrontCW,  "F"),
				new Movement(CubeSolver::moveFrontCCW, "G"),
				new Movement(CubeSolver::moveFront2,  "FF"),
				new Movement(CubeSolver::moveLeftCW,   "L"),
				new Movement(CubeSolver::moveLeftCCW,  "M"),
				new Movement(CubeSolver::moveLeft2,   "LL"),
			};

			// Update previous move
			previousMove = path.isEmpty() ? "" : String.valueOf(path.charAt(path.length()-1));

			// Iterate through moves and add to queue
			for(Movement movement : moveFunctions){
				if(prune(previousMove, movement.getMoveStr())){
					continue;
				}
				// Create new instance of a cube
				int[] newCube = currentCube.clone();
				movement.getMoveFunction().move(newCube);
				queue.offer(new StatePathPair(newCube, path + movement.getMoveStr()));
				// Delete new instance for garbage collection
				newCube = null;
			}
		}
		return(null);
	}

	// Function: Prune
	// Purpose: Will stop a branch from creating child nodes on specific cases that would be useless
	// Parameters: The previous move and the current move
	// Precondition: Previous move must be defined, not empty
	// Return: True if pointless, cut branch
	//		 : False if not pointless, create child nodes
	public static boolean prune(String pre, String curr){
		if(pre.equals(curr)) return(true);
		else if(pre.equals("U")){
			if(curr.equals("V"))  return(true);
			if(curr.equals("UU")) return(true);
		}
		else if(pre.equals("V")){
			if(curr.equals("U"))  return(true);
			if(curr.equals("UU")) return(true);
		}
		else if(pre.equals("F")){
			if(curr.equals("G"))  return(true);
			if(curr.equals("FF")) return(true);
		}
		else if(pre.equals("G")){
			if(curr.equals("F"))  return(true);
			if(curr.equals("FF")) return(true);
		}
		else if(pre.equals("L")){
			if(curr.equals("M"))  return(true);
			if(curr.equals("LL")) return(true);
		}
		else if(pre.equals("M")){
			if(curr.equals("L"))  return(true);
			if(curr.equals("LL")) return(true);
		}
		return(false);

	}

	// Function: checkSolved
	// Purpose: Check if the cube is in a solved state
	// Parameter: The current state of the cube
	// Return: True if it is solved (three adjacent sides are all solved)
	//		 : False otherwise
	public static boolean checkSolved(int[] cube){
		if(cube[0] != cube[1]){
			return(false);
		}
		else{
			if(        (cube[0]  == cube[1] ) && (cube[1]  == cube[2])  && (cube[2]  == cube[3])){
				if(    (cube[16] == cube[17]) && (cube[17] == cube[18]) && (cube[18] == cube[19])){
					if((cube[8]  == cube[9] ) && (cube[9]  == cube[10]) && (cube[10] == cube[11])){
						return(true);
					}
				}
			}
		}
		return(false);
	}

	// Function: concatenateArrays
	// Helper to solve function, will transform input of 6 arrays into 1 array for better memory
	public static int[] concatenateArrays(int[]... arrays){
		int[] outCube = new int[24];

		int i = 0;
		for(int[] array : arrays){
			System.arraycopy(array, 0, outCube,i,array.length);
			i = i+ 4;
		}
		return(outCube);
	}

	// Function: arrayToString
	// Helper to solveTree function, used to store data in hash set
	public static String arrayToString(int[] array){
		StringBuilder sb = new StringBuilder();
		for(int num : array){
			sb.append(num);
		}
		return(sb.toString());
	}

	// Class movement
	// Helper to solveTree function, easier calling of moves
	public static class Movement{
		private final MoveFunction moveFunction;
		private final String moveStr;

		public Movement(MoveFunction moveFunction, String moveStr){
			this.moveFunction = moveFunction;
			this.moveStr = moveStr;
		}

		public MoveFunction getMoveFunction(){
			return(moveFunction);
		}

		public String getMoveStr(){
			return(moveStr);
		}
	}

	// MoveFunction interface
	// Helper to solveTree function, easier calling of moves
	@FunctionalInterface
	public interface MoveFunction{
		void move(int[] cube);
	}

	// StatePathPair class
	// Object used to push/pull an array and a string from the queue at the same time
	public static class StatePathPair{
		private final int[] cube;
		private final String path;

		public StatePathPair(int[] cube, String path){
			this.cube = cube;
			this.path = path;
		}

		public int[] getCube(){
			return(cube);
		}

		public String getPath(){
			return(path);
		}
	}
	

	// Functions move_'face'_'direction'
    // face: upper | down | front | back | left |right
    // direction: clockwise | counterclockwise
    // Purpose: Will rotate the face of the cube in the direction 
	public static void moveUpperCW(int[] cube){
		int temp,temp2,temp3;
		temp = cube[8];
		temp2 = cube[9];
		temp3 = cube[0];
		cube[8] = cube[20];
		cube[9] = cube[21];
		cube[20] = cube[12];
		cube[21] = cube[13];
		cube[12] = cube[16];
		cube[13] = cube[17];
		cube[16] = temp;
		cube[17] = temp2;
		cube[0] = cube[2];
		cube[2] = cube[3];
		cube[3] = cube[1];
		cube[1] = temp3;
	}

	public static void moveUpperCCW(int[] cube){
		int temp,temp2,temp3;
		temp = cube[8];
		temp2 = cube[9];
		temp3 = cube[0];
		cube[8] = cube[16];
		cube[9] = cube[17];
		cube[16] = cube[12];
		cube[17] = cube[13];
		cube[12] = cube[20];
		cube[13] = cube[21];
		cube[20] = temp;
		cube[21] = temp2;
		cube[0] = cube[1];
		cube[1] = cube[3];
		cube[3] = cube[2];
		cube[2] = temp3;
	}

	public static void moveUpper2(int[] cube){
		int temp,temp2,temp3;
		temp = cube[8];
		temp2 = cube[9];
		cube[8] = cube[12];
		cube[9] = cube[13];
		cube[12] = temp;
		cube[13] = temp2;
		temp = cube[16];
		temp2 = cube[17];
		cube[16] = cube[20];
		cube[17] = cube[21];
		cube[20] = temp;
		cube[21] = temp2;
		temp3 = cube[0];
		cube[0] = cube[3];
		cube[3] = temp3;
		temp3 = cube[1];
		cube[1] = cube[2];
		cube[2] = temp3;
	}

	public static void moveFrontCW(int[] cube){
		int temp,temp2,temp3;
		temp = cube[2];
		temp2 = cube[3];
		temp3 = cube[8];
		cube[2] = cube[19];
		cube[3] = cube[17];
		cube[19] = cube[5];
		cube[17] = cube[4];
		cube[4] = cube[22];
		cube[5] = cube[20];
		cube[22] = temp2;
		cube[20] = temp;
		cube[8] = cube[10];
		cube[10] = cube[11];
		cube[11] = cube[9];
		cube[9] = temp3;
	}

	public static void moveFrontCCW(int[] cube){
		int temp,temp2,temp3;
		temp = cube[2];
		temp2 = cube[3];
		temp3 = cube[8];
		cube[2] = cube[20];
		cube[3] = cube[22];
		cube[20] = cube[5];
		cube[22] = cube[4];
		cube[5] = cube[19];
		cube[4] = cube[17];
		cube[19] = temp;
		cube[17] = temp2;
		cube[8] = cube[9];
		cube[9] = cube[11];
		cube[11] = cube[10];
		cube[10] = temp3;
	}

	public static void moveFront2(int[] cube){
		int temp,temp2,temp3;
		temp = cube[2];
		temp2 = cube[3];
		cube[2] = cube[5];
		cube[3] = cube[4];
		cube[5] = temp;
		cube[4] = temp2;
		temp = cube[20];
		temp2 = cube[22];
		cube[20] = cube[19];
		cube[22] = cube[17];
		cube[19] = temp;
		cube[17] = temp2;
		temp3 = cube[8];
		cube[8] = cube[11];
		cube[11] = temp3;
		temp3 = cube[9];
		cube[9] = cube[10];
		cube[10] = temp3;
	}

	public static void moveLeftCW(int[] cube){
		int temp,temp2,temp3;
		temp = cube[0];
		temp2 = cube[2];
		temp3 = cube[16];
		cube[0] = cube[15];
		cube[2] = cube[13];
		cube[15] = cube[4];
		cube[13] = cube[6];
		cube[4] = cube[8];
		cube[6] = cube[10];
		cube[8] = temp;
		cube[10] = temp2;
		cube[16] = cube[18];
		cube[18] = cube[19];
		cube[19] = cube[17];
		cube[17] = temp3;
	}

	public static void moveLeftCCW(int[] cube){
		int temp,temp2,temp3;
		temp = cube[0];
		temp2 = cube[2];
		temp3 = cube[16];
		cube[0] = cube[8];
		cube[2] = cube[10];
		cube[8] = cube[4];
		cube[10] = cube[6];
		cube[4] = cube[15];
		cube[6] = cube[13];
		cube[15] = temp;
		cube[13] = temp2;
		cube[16] = cube[17];
		cube[17] = cube[19];
		cube[19] = cube[18];
		cube[18] = temp3;
	}

	public static void moveLeft2(int[] cube){
		int temp,temp2,temp3;
		temp = cube[0];
		temp2 = cube[2];
		cube[0] = cube[4];
		cube[2] = cube[6];
		cube[4] = temp;
		cube[6] = temp2;
		temp = cube[8];
		temp2 = cube[10];
		cube[8] = cube[15];
		cube[10] = cube[13];
		cube[15] = temp;
		cube[13] = temp2;
		temp3 = cube[16];
		cube[16] = cube[19];
		cube[19] = temp3;
		temp3 = cube[17];
		cube[17] = cube[18];
		cube[18] = temp3;
	}
}


