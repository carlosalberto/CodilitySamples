
using System;

public class Tester
{
	public static int BinarySearch (int [] A, int value)
	{
		int start = 0;
		int end = A.Length - 1;

		while (start <= end) {
			int middle = (start + end) / 2;
			if (A [middle] == value)
				return middle;

			if (A [middle] > value)
				end = middle - 1;
			else
				start = middle + 1;
		}

		return -1;
	}

	public static void Main ()
	{
		Console.WriteLine (BinarySearch (new int [0], 10));
		Console.WriteLine (BinarySearch (new [] { 0 }, 10));
		Console.WriteLine (BinarySearch (new [] { 0, 11 }, 10));
		Console.WriteLine ();

		Console.WriteLine (BinarySearch (new [] { 1, 2, 3, 4, 5 }, 3));
		Console.WriteLine (BinarySearch (new [] { 1, 2, 3, 4, 5, 6 }, 3));
		Console.WriteLine (BinarySearch (new [] { 1, 2, 3, 4, 5, 6 }, 1));
		Console.WriteLine (BinarySearch (new [] { 1, 2, 3, 4, 5, 6 }, 6));
		Console.WriteLine (BinarySearch (new [] { 1, 2, 3, 4, 5, 6 }, 9));
	}
}

