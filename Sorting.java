/*
A bunch of sorting algorithms simplified
This was written a long time ago so I'm not sure how effective it is
*/
import java.util.*;

class Sorting
{
	public static void main (String[] args)
	{
		int length = 10000; //Change this to change length of array...
		Sorting s = new Sorting();
		Random r = new Random();
		//Create random array for sorting
		int[] toSort = new int[length], sorted;
		for (int i = 0; i < toSort.length; i++) toSort[i] = r.nextInt(toSort.length);
		System.out.println("Generated a random array of " + toSort.length + " integers.");
		Date start, end;
		
		//Count
		start = new Date();
		sorted = s.count(toSort);
		end = new Date();
		System.out.println("Count sort done in " + (end.getTime() - start.getTime()) + " milliseconds.");
		if (s.correct(sorted)) System.out.println("Count sort is correct.");
		
		//Quick
		start = new Date();
		sorted = s.quick(toSort);
		end = new Date();
		System.out.println("Quick sort done in " + (end.getTime() - start.getTime()) + " milliseconds.");
		if (s.correct(sorted)) System.out.println("Quick sort is correct.");
		
		//Bubble
		start = new Date();
		sorted = s.bubble(toSort);
		end = new Date();
		System.out.println("Bubble sort done in " + (end.getTime() - start.getTime()) + " milliseconds.");
		if (s.correct(sorted)) System.out.println("Bubble sort is correct.");
	}
	
	public void printArray(int[] array)
	{
		for (int i = 0; i < array.length; i++)
		{
			System.out.print(array[i]);
			if (i != array.length - 1) System.out.print(", ");
		}
		System.out.println();
	}
	
	public boolean correct(int[] toCheck)
	{
		boolean check = true;
		for (int i = 0; i < toCheck.length - 1; i++)
		{
			if (toCheck[i] > toCheck[i+1])
			{
				check = false;
				break;
			}
		}
		return check;
	}
	
	public int[] bubble(int[] toSort)
	{
		//Most common sorting method - not always fastest (but this has been optimized for max efficiency)
		int length = toSort.length;
		int max = length - 1;
		int i, temp;
		boolean swapped = false;
		while (true)
		{
			swapped = false;
			for (i = 0; i < max; i++)
			{
				if (toSort[i] > toSort[i+1])
				{
					temp = toSort[i];
					toSort[i] = toSort[i+1];
					toSort[i+1] = temp;
					swapped = true;
				}
			}
			if (!swapped) break;
			max--;
		}
		return toSort;
	}
	
	public int[] bog(int[] toSort)
	{
		//I recommend you don't use this!!!!!!!!!!!! (really slow)
		int[] toReturn = new int[toSort.length];
		while (true)
		{		
			boolean[] taken = new boolean[toReturn.length];
			Random r = new Random();
			for (int x = 0; x < toSort.length; x++)
			{
				while (true)
				{
					int a = r.nextInt(toReturn.length);
					if (!taken[a])
					{
						taken[a] = true;
						toReturn[a] = toSort[x];
						break;
					}
				}
			}
			if (correct(toReturn)) break;
		}
		return toReturn;
	}
	
	public int[] quick(int[] toSort)
	{
		//Modified quicksort - should be relatively efficient
		int[] toReturn = new int[toSort.length];
		if (toSort.length <= 1 || correct(toSort))
		{
			toReturn = toSort;
		}
		else
		{
			Random r = new Random();
			int mid = r.nextInt(toSort.length - 1);
			int[] less = new int[toSort.length], more = new int[toSort.length];
			int lP = 0, mP = 0;
			for (int x = 0; x < toSort.length; x++)
			{
				if (toSort[x] < toSort[mid])
				{
					less[lP] = toSort[x];
					lP++;
				}
				else
				{
					more[mP] = toSort[x];
					mP++;
				}
			}
			less = cl(less, lP);
			more = cl(more, mP);
			if (less.length > 1) less = quick(less);
			if (more.length > 1) more = quick(more);
			toReturn = join(less, more);
		}
		return toReturn;
	}
	
	public int[] cl(int[] change, int newMax)
	{
		//Change length function - shortens array
		if (newMax < change.length)
		{
			int[] toReturn = new int[newMax];
			for (int x = 0; x < newMax; x++)
			{
				toReturn[x] = change[x];
			}
			return toReturn;
		}
		else return change;
	}
	
	public int[] join(int[] array1, int[] array2)
	{
		//Joining function - literally merges array1 and array 2 together
		int[] toReturn = new int[array1.length + array2.length];
		for (int x = 0; x < array1.length; x++) toReturn[x] = array1[x];
		for (int x = 0; x < array2.length; x++) toReturn[x+array1.length] = array2[x];
		return toReturn;
	}
	
	public int[] count(int[] toSort)
	{
		//Really simple and fast way of sorting an array of POSITIVE integers
		int[] countLog, toReturn;
		int x, y, length = toSort.length, step = 0;
		countLog = new int[length];
		toReturn = new int[length];
		for (x = 0; x < length; x++) countLog[toSort[x]]++;
		for (x = 0; x < length; x++)
		{
			if (countLog[x] > 0)
			{
				for (y = 0; y < countLog[x]; y++)
				{
					toReturn[step] = x;
					step++;
				}
			}
		}
		return toReturn;
	}
}