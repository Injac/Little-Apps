/*
Like the Boggle sample this also requires englishwords.txt
This basically just checks if there are any words that someone may have
based their iOS passcode on
To run, execute java Passcode 1234
*/
import java.io.*;
import java.util.*;

class Passcode
{
	public static void main(String[] args)
	{
		Passcode pc = new Passcode();
		String toCheck = args[0];
		System.out.println("Going to check code " + toCheck);
		int a = Integer.parseInt(toCheck.substring(0,1)), b = Integer.parseInt(toCheck.substring(1,2)), c = Integer.parseInt(toCheck.substring(2,3)), d = Integer.parseInt(toCheck.substring(3,4));
		String[] p = new String[10];
		p[0] = " ";
		p[1] = " ";
		p[2] = "abc";
		p[3] = "def";
		p[4] = "ghi";
		p[5] = "jkl";
		p[6] = "mno";
		p[7] = "pqrs";
		p[8] = "tuv";
		p[9] = "wxyz";
		try
		{
			FileInputStream fstream = new FileInputStream("englishwords.txt");
			DataInputStream in = new DataInputStream(fstream);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String line;
			ArrayList<String> valids = new ArrayList<String>();
			while ((line = br.readLine()) != null)
			{
				if (line.length() == 4)
				{
					line = line.toLowerCase();
					if (pc.contains(p[a], line.charAt(0)) && pc.contains(p[b], line.charAt(1)) && pc.contains(p[c], line.charAt(2)) &&pc.contains(p[d], line.charAt(3))) System.out.println(line);
				}
			}
		}
		catch (Exception e)
		{
			System.out.println("Yeah, an error occured");
		}
	}
	
	public boolean contains(String options, char toCheck)
	{
		for (int i = 0; i < options.length(); i++)
		{
			if (options.charAt(i) == toCheck)  return true;
		}
		return false;
	}
}