using System;
using System.Collections.Generic;

public class Tester
{
	public static int Solution (int [] W, int k)
	{
		int N = W.Length;
		var fatso = new LinkedList<int> ();
		var skinny = new LinkedList<int> ();

		for (int i = 0; i < N - 1; i++)
			if (W [i] + W [N - 1] <= k)
				skinny.AddLast (W [i]);
			else
				fatso.AddLast (W [i]);

		fatso.AddLast (W [N - 1]);

		int canoes = 0;

		while (fatso.Count > 0) {
			fatso.RemoveLast ();
			if (skinny.Count > 0)
				skinny.RemoveLast ();

			canoes++;

			if (skinny.Count > 0 && fatso.Count == 0) {
				fatso.AddLast (skinny.Last.Value);
				skinny.RemoveLast ();
			}

			while (fatso.Count > 1 && fatso.First.Value + fatso.Last.Value <= k) {
				skinny.AddLast (fatso.First.Value);
				fatso.RemoveFirst ();
			}
		}

		return canoes;
	}

	static void Main ()
	{
		Console.WriteLine (Solution (new int [1], 1));
		Console.WriteLine (Solution (new int [] { 0, 1 }, 1));
		Console.WriteLine (Solution (new int [] { 1, 1, 1, 1, 1 }, 1));
		Console.WriteLine ();

		Console.WriteLine (Solution (new int [] {13, 14, 17, 21, 33, 35}, 35));
		Console.WriteLine (Solution (new int [] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 10));
	}
}

