/*
I am complete cheat at Boggle so I use this instead of playing properly
You'll need the englishwords.txt folder from the repo as well
To run the app use java boggle abcdefghijklmnop where each letter represents the letter in the grid
The first four letters represent the first row, the second four the second, etc
The code is a bit messy but it works!
*/

import java.io.*;
import java.util.*;
class boggle
{
	public static void main(String args[])
	{
		boggle b = new boggle();
		String gridString = args[0];
		try
		{
			FileInputStream fstream = new FileInputStream("englishwords.txt");
			DataInputStream in = new DataInputStream(fstream);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String line;
			ArrayList<String> valids = new ArrayList<String>();
			while ((line = br.readLine()) != null)
			{
				String original = line;
				line = line.trim().toLowerCase().replace("qu", "q");
				if (line.length() >= 3 && line.length() <= 16)
				{
					boolean safe = true;
					for (int i = 0; i < line.length(); i++)
					{
						if (b.occur(line, line.charAt(i)) > b.occur(gridString, line.charAt(i)))
						{
							safe = false;
							break;
						}
					}
					if (safe)
					{
						
						String g = gridString.toString();
						for (int i = 0; i < 16; i++)
						{
							if (g.charAt(i) == line.charAt(0))
							{
								int x = i % 4;
								int y = (i - x) / 4;
								int surrounds = i;
								boolean[] used = new boolean[16];
								used[i] = true;
								for (int c = 0; c < line.length() - 1; c++)
								{
									StringBuilder sb = new StringBuilder(g);
										sb.setCharAt(surrounds, Character.toUpperCase(sb.charAt(surrounds)));
										g = sb.toString();
									surrounds = b.surroundedBy(x,y,g,line.charAt(c+1));
									if (surrounds >= 0)
									{
										x = surrounds % 4;
										y = (surrounds - x) / 4;
										used[surrounds] = true;
									}
									else
									{
										safe = false;
										break;
									}
								}
								if (safe) break;
							}
						}
						if (safe) valids.add(original);
					}
				}
			}
			String[] validArray = new String[valids.size()];
			validArray = valids.toArray(validArray);
			for (int k = 0; k < validArray.length; k++)
			{
				int greatestIndex = 0;
				int greatestLength = 0;
				for (int l = 0; l < validArray.length; l++)
				{
					if (validArray[l].length() > greatestLength)
					{
						greatestLength = validArray[l].length();
						greatestIndex = l;
					}
				}
				System.out.println(String.valueOf((k + 1)) + ": " + validArray[greatestIndex]);
				validArray[greatestIndex] = "";
				if (k > 150) break;
			}
		}
		catch (Exception e)
		{
			System.out.println(e.getMessage());
		}
	}
	
	public int surroundedBy(int x, int y, String gridString, char c)
	{
		if (x > 0 && y > 0)
		{
			if (gridString.charAt((x-1) + ((y-1)*4)) == c) return (x-1) + ((y-1)*4);
		}
		if (y > 0)
		{
			if (gridString.charAt(x + ((y-1)*4)) == c) return x + ((y-1)*4);
		}
		if (y > 0 && x < 3)
		{
			if (gridString.charAt((x+1) + ((y-1)*4)) == c) return (x+1) + ((y-1)*4);
		}
		if (x > 0)
		{
			if (gridString.charAt(x - 1 + (y*4)) == c) return x - 1 + (y*4);
		}
		if (x < 3)
		{
			if (gridString.charAt((x+1) + (y*4)) == c) return (x+1) + (y*4);
		}
		if (x > 0 && y < 3)
		{
			if (gridString.charAt((x-1) + ((y+1)*4)) == c) return (x-1) + ((y+1)*4);
		}
		if (y < 3)
		{
			if (gridString.charAt(x + ((y+1)*4)) == c) return x + ((y+1)*4);
		}
		if (x < 3 && y < 3)
		{
			if (gridString.charAt((x+1) + ((y+1)*4)) == c)  return (x+1) + ((y+1)*4);
		}
		return -1;
	}
	
	public int occur(String haystack, char needle)
	{
		int count = 0;
		for (int i = 0; i < haystack.length(); i++)
		{
			if (haystack.charAt(i) == needle) count++;
		}
		return count;
	}
}