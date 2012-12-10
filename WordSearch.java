import java.io.*;

class WordSearch
{
	public static void main(String[] args)
	{
		String searchTerm = args[0];
		System.out.println(searchTerm);
		String[] array = new String[60000];
		int next = 0;
		try
		{
			FileInputStream fstream = new FileInputStream("englishwords.txt");
			DataInputStream in = new DataInputStream(fstream);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String line;
			while ((line = br.readLine()) != null)
			{
				boolean good = true;
				if (searchTerm.length() == line.trim().length())
				{
					for (int a = 0; a < searchTerm.length(); a++)
					{
						if (!(searchTerm.charAt(a) != '-' && searchTerm.charAt(a) == line.charAt(a)))
						{
							good = false;
							break;
						}
					}
				}
				else good = false;
				if (good)
				{
					array[next] = line;
					next++;
				}
			}
		}
		catch (Exception e)
		{
			System.err.println("Error: " + e.getMessage());
		}
		for (int i = 0; i < next; i++)
		{
			System.out.println(array[i]);
		}
	}
}