import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;



public class Solver{
	public static void main(String[] args){
		int[] cube = new int[]{0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5};

		System.out.print("Main");
		display(cube);
		move_upper_ccw(cube);
		System.out.print("Main");
		display(cube);


		int[] solve_path = solveTree(cube);
		if(solve_path == null){
			System.out.println("Solver failed");
		}
		else{
			displayPath(solve_path);
		}
		
	}	
	
	static class Cube{
		int[] cube;
		int[] path;
		int depth;

		Cube(int[] cube, int[] path, int depth){
			this.cube = cube;
			this.path = path;
			this.depth = depth;
		}
	}


	public static void display(int[] cube){
		System.out.print("[");
		for(int i = 0; i < cube.length; i++){
			System.out.print("" + cube[i]);
			if((i+1) % 4 != 0){
				System.out.print(",");
			}

			if((i+1) % 4 == 0){
				System.out.print("]");
				if(i < 22) System.out.print(".[");
			}
		}
		System.out.println();
	}

	public static void displayPath(int[] path){
		System.out.println();
		for(int i = 0; i < path.length; i++){
			if(path[i] == 0) System.out.print("U -");
			if(path[i] == 1) System.out.print("U'-");
			if(path[i] == 2) System.out.print("F -");
			if(path[i] == 3) System.out.print("F'-");
			if(path[i] == 4) System.out.print("L -");
			if(path[i] == 5) System.out.print("L'-");
		}

		System.out.println();
	}


	public static int[] solveTree(int[] inCube){
		Queue<Cube> queue = new ArrayDeque<>();
		Set<String> visited = new HashSet<>();
		int maxDepth = 1;

		queue.add(new Cube(inCube, new int[]{}, 0));

		while(!queue.isEmpty()){
			Cube currentState = queue.poll();
			int[] currentCube = currentState.cube;
			int[] currentPath = currentState.path;
			int depth = currentState.depth;

			if(depth > maxDepth){
				System.out.println("Depth Limit Reached.");
				break;
			}

			if(check_solved(currentCube)){
				return(currentPath);
			}

			String state = Arrays.toString(currentCube);
			if(visited.contains(state)){
				continue;
			}
			visited.add(state);

			int[] newCube;
			int[] newPath;

			// Add Move Upper CW to queue
			newCube = Arrays.copyOf(currentCube,currentCube.length);
			newPath = Arrays.copyOf(currentPath,currentPath.length +1);
			newPath[newPath.length -1 ] = 0;
			System.out.println("\nTry Upper CW");
			display(newCube);
			move_upper_cw(newCube);
			/////////////////////////////////////////////////////////////////////////////////
			display(newCube);
			queue.add(new Cube(newCube,newPath,depth+1));
			move_upper_ccw(newCube);

			// Add Move Upper CCW to queue
			newCube = Arrays.copyOf(currentCube,currentCube.length);
			newPath = Arrays.copyOf(currentPath,currentPath.length +1);
			newPath[newPath.length -1 ] = 1;
			System.out.println("\nTry Upper CCW");
			display(newCube);
			move_upper_ccw(newCube);
			/////////////////////////////////////////////////////////////////////////////////
			display(newCube);
			queue.add(new Cube(newCube,newPath,depth+1));
			move_upper_cw(newCube);

			// Add Move Front CW to queue
			newCube = Arrays.copyOf(currentCube,currentCube.length);
			newPath = Arrays.copyOf(currentPath,currentPath.length +1);
			newPath[newPath.length -1 ] = 2;
			System.out.println("\nTry Front CW");
			display(newCube);
			move_front_cw(newCube);
			/////////////////////////////////////////////////////////////////////////////////
			display(newCube);
			queue.add(new Cube(newCube,newPath,depth+1));
			move_front_ccw(newCube);

			// Add Move Front CCW to queue
			newCube = Arrays.copyOf(currentCube,currentCube.length);
			newPath = Arrays.copyOf(currentPath,currentPath.length +1);
			newPath[newPath.length -1 ] = 3;
			System.out.println("\nTry Front CCW");
			display(newCube);
			move_front_ccw(newCube);
			/////////////////////////////////////////////////////////////////////////////////
			display(newCube);
			queue.add(new Cube(newCube,newPath,depth+1));
			move_front_cw(newCube);

			// Add Move Left CW to queue
			newCube = Arrays.copyOf(currentCube,currentCube.length);
			newPath = Arrays.copyOf(currentPath,currentPath.length +1);
			newPath[newPath.length -1 ] = 3;
			System.out.println("\nTry Left CW");
			display(newCube);
			move_left_cw(newCube);
			/////////////////////////////////////////////////////////////////////////////////
			display(newCube);
			queue.add(new Cube(newCube,newPath,depth+1));
			move_left_ccw(newCube);

			// Add Move Left CCW to queue
			newCube = Arrays.copyOf(currentCube,currentCube.length);
			newPath = Arrays.copyOf(currentPath,currentPath.length +1);
			newPath[newPath.length -1 ] = 3;
			System.out.println("\nTry Left CCW");
			display(newCube);
			move_left_ccw(newCube);
			/////////////////////////////////////////////////////////////////////////////////
			display(newCube);
			queue.add(new Cube(newCube,newPath,depth+1));
			move_left_cw(newCube);
		}
		return(null);

	}

	public static boolean check_solved(int[] in_cube){
		System.out.print("... Checking.");
		display(in_cube);
		if(in_cube[0] != in_cube[1]){
			return(false);
		}
		else{
			if(        (in_cube[0]  == in_cube[1] ) && (in_cube[1]  == in_cube[2])  && (in_cube[2]  == in_cube[3])){
				if(    (in_cube[16] == in_cube[17]) && (in_cube[17] == in_cube[18]) && (in_cube[18] == in_cube[19])){
					if((in_cube[8]  == in_cube[9] ) && (in_cube[9]  == in_cube[10]) && (in_cube[10] == in_cube[11])){
						System.out.println("... Solved");
						return(true);
					}
				}
			}
			System.out.println();
			return(false);
		}
	}
		
	

	public static void move_upper_cw(int[] cube){
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

	public static void move_upper_ccw(int[] cube){
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

	public static void move_front_cw(int[] cube){
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

	public static void move_front_ccw(int[] cube){
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

	public static void move_left_cw(int[] cube){
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

	public static void move_left_ccw(int[] cube){
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
}


