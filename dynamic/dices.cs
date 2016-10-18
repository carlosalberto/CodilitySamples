
using System;

public class Tester
{
	public static int Solution (int [] A)
	{
		int n = A.Length;
		var dp = new int [n];
		dp [0] = A [0];

		for (int i = 1; i < n; i++) {
			dp [i] = Int32.MinValue;

			for (int steps = Math.Min (6, i); steps > 0; steps--)
				dp [i] = Math.Max (dp [i], dp [i - steps] + A [i]);
		}

		//PrintArray (dp);
		return dp [n - 1];
	}

	static void PrintArray (int [] A)
	{
		Console.Write ("[");
		foreach (int value in A)
			Console.Write (" " + value);
		Console.WriteLine (" ]");
	}

	static void Main ()
	{
		Console.WriteLine (Solution (new [] { 1, -2, 0, 9, -1, -2 })); // 8
		Console.WriteLine (Solution (new [] { 1, -2, 0, 9, -1, -2, -2, -2, -2, -2, -2 })); // 7
		Console.WriteLine (Solution (new [] { 1, -2, 0, 9, -1, 100 })); // 110
	}
}

