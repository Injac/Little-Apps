using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

namespace ColorPalette
{
  class MainClass
	{
		public static void Main (string[] args)
		{
			string filenameIn, filenameOut;
			if (args.Length == 0) {
				Console.WriteLine ("Please enter a file to process: ");
				filenameIn = Console.ReadLine ();
			} else
				filenameIn = args [0];
			filenameOut = filenameIn.Substring (0, filenameIn.LastIndexOf (".")) + "hues.png";
			Bitmap bitmap = (Bitmap)Image.FromFile (filenameIn);
			ColorRGB[] rgbArray = new ColorRGB[bitmap.Width * bitmap.Height];
			getRGB (bitmap, 0, 0, bitmap.Width, bitmap.Height, rgbArray, 0, bitmap.Width);
			int[,] shades = new int[360, 255];
			int mean = 0;
			for (int n = 0; n < rgbArray.Length; n++) {
				int h = (int)Math.Max(0, Math.Floor(360.0f * rgbArray[n].H) - 1);
				int s = (int)Math.Max (0, Math.Floor(255.0f * rgbArray[n].S - 1));
				shades[h, s]++;
			}
			for (int x = 0; x < 360; x++) {
				for (int y = 0; y < 255; y++) {
					mean += shades[x, y];
				}
			}

			mean /= 360 * 255;
			Bitmap newImage = new Bitmap (255, 360);
			for (int y = 0; y < 360; y++) {
				for (int x = 0; x < 255; x++) {
					double hue = (double)y / 360.0;
					double saturation = (double)x / 255.0;
					double lightness = 1 - Math.Min(0.5, (double)shades[y, x] / (double)mean * 0.5);
					newImage.SetPixel(x, y, (Color)ColorRGB.FromHSL(hue, saturation, lightness));
				}
			}
			Image finalImage = (Image)newImage;
			finalImage.Save (filenameOut);
		}

		public static void getRGB(Bitmap image, int startX, int startY, int w, int h, ColorRGB[] rgbArray, int offset, int scansize)
		{
			const int PixelWidth = 3;
			const PixelFormat PixelFormat = PixelFormat.Format24bppRgb;
			
			// En garde!
			if (image == null) throw new ArgumentNullException("image");
			if (rgbArray == null) throw new ArgumentNullException("rgbArray");
			if (startX < 0 || startX + w > image.Width) throw new ArgumentOutOfRangeException("startX");
			if (startY < 0 || startY + h > image.Height) throw new ArgumentOutOfRangeException("startY");
			if (w < 0 || w > scansize || w > image.Width) throw new ArgumentOutOfRangeException("w");
			if (h < 0 || (rgbArray.Length < offset + h * scansize) || h > image.Height) throw new ArgumentOutOfRangeException("h");
			
			BitmapData data = image.LockBits(new Rectangle(startX, startY, w, h), System.Drawing.Imaging.ImageLockMode.ReadOnly, PixelFormat);
			try
			{
				byte[] pixelData = new Byte[data.Stride];
				for (int scanline = 0; scanline < data.Height; scanline++)
				{
					Marshal.Copy(data.Scan0 + (scanline * data.Stride), pixelData, 0, data.Stride);
					for (int pixeloffset = 0; pixeloffset < data.Width; pixeloffset++)
					{
						// PixelFormat.Format32bppRgb means the data is stored
						// in memory as BGR. We want RGB, so we must do some 
						// bit-shuffling.
						rgbArray[offset + (scanline * scansize) + pixeloffset] = new ColorRGB(Color.FromArgb(
							pixelData[pixeloffset * PixelWidth + 2],    // R 
							pixelData[pixeloffset * PixelWidth + 1],    // G
							pixelData[pixeloffset * PixelWidth]));                // B
					}
				}
			}
			finally
			{
				image.UnlockBits(data);
			}
		}
	}

	public class ColorRGB
	{
		public byte R;
		public byte G;
		public byte B;
		public byte A;
		
		public ColorRGB()
		{
			R = 255;
			G = 255;
			B = 255;
			A = 255;
		}
		
		public ColorRGB(Color value)
		{
			this.R = value.R;
			this.G = value.G;
			this.B = value.B;
			this.A = value.A;
		}
		public static implicit operator Color(ColorRGB rgb)
		{
			Color c = Color.FromArgb(rgb.A, rgb.R, rgb.G, rgb.B);
			return c;
		}
		public static explicit operator ColorRGB(Color c)
		{
			return new ColorRGB(c);
		}
		
		
		// Given H,S,L in range of 0-1
		// Returns a Color (RGB struct) in range of 0-255
		public static ColorRGB FromHSL(double H, double S, double L)
		{
			return FromHSLA(H, S, L, 1.0);
		}
		
		// Given H,S,L,A in range of 0-1
		// Returns a Color (RGB struct) in range of 0-255
		public static ColorRGB FromHSLA(double H, double S, double L, double A)
		{
			double v;
			double r, g, b;
			if (A > 1.0)
				A = 1.0;
			
			r = L;   // default to gray
			g = L;
			b = L;
			v = (L <= 0.5) ? (L * (1.0 + S)) : (L + S - L * S);
			if (v > 0)
			{
				double m;
				double sv;
				int sextant;
				double fract, vsf, mid1, mid2;
				
				m = L + L - v;
				sv = (v - m) / v;
				H *= 6.0;
				sextant = (int)H;
				fract = H - sextant;
				vsf = v * sv * fract;
				mid1 = m + vsf;
				mid2 = v - vsf;
				switch (sextant)
				{
				case 0:
					r = v;
					g = mid1;
					b = m;
					break;
				case 1:
					r = mid2;
					g = v;
					b = m;
					break;
				case 2:
					r = m;
					g = v;
					b = mid1;
					break;
				case 3:
					r = m;
					g = mid2;
					b = v;
					break;
				case 4:
					r = mid1;
					g = m;
					b = v;
					break;
				case 5:
					r = v;
					g = m;
					b = mid2;
					break;
				}
			}
			ColorRGB rgb = new ColorRGB();
			rgb.R = Convert.ToByte(r * 255.0f);
			rgb.G = Convert.ToByte(g * 255.0f);
			rgb.B = Convert.ToByte(b * 255.0f);
			rgb.A = Convert.ToByte(A * 255.0f);
			return rgb;
		}
		
		// Hue in range from 0.0 to 1.0
		public float H
		{
			get
			{
				// Use System.Drawing.Color.GetHue, but divide by 360.0F 
				// because System.Drawing.Color returns hue in degrees (0 - 360)
				// rather than a number between 0 and 1.
				return ((Color)this).GetHue() / 360.0F;
			}
		}
		
		// Saturation in range 0.0 - 1.0
		public float S
		{
			get
			{
				return ((Color)this).GetSaturation();
			}
		}
		
		// Lightness in range 0.0 - 1.0
		public float L
		{
			get
			{
				return ((Color)this).GetBrightness();
			}
		}
	}
}
