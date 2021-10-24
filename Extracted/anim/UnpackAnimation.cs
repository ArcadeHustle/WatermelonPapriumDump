// Code by Hpman 

// $ mcs -out:UnpackAnimation.exe UnpackAnimation.cs -r:System.Drawing.dll 

using System;
using System.IO;
using System.Drawing;

namespace UnpackAnimation {
	class Decode {
		static void Main(string[] args) {
			Console.WriteLine("Reading packed animation data!");

			Bitmap blocks;
			blocks = new Bitmap(512,512);
			byte[] data;
			data = File.ReadAllBytes(@"unpk_0x0c0000.bin");

			Bitmap bmp = new Bitmap(512,512);
			bmp.MakeTransparent();
			Graphics gfx = Graphics.FromImage(bmp);

			uint addr = 0x0;
			//uint ptr = addr & 0xffffff;
			uint ptr = 0x7e754;

			int count = data[ptr];
			Console.WriteLine(count);
			ptr +=2;

			int posX=0, posY=0;

			for (int s = 0; s < count; s++)
			{
				if (s == 0)
				{
					posX = 256 + (sbyte)data[ptr];
					posY = 256 + (sbyte)data[ptr] + 1;
				}
				else
				{
					posX += (sbyte)data[ptr];
					posY += (sbyte)data[ptr + 1];
				}
				int sizeX = ((data[ptr + 2] & 0xf) >> 2) +1;
				int sizeY = (data[ptr + 2] & 0x3) +1;
				int offset = data[ptr+7];
				int block = (data[ptr +4] << 8) + data[ptr + 5];

				int blkX = (block & 0x1f) << 5;
				int blkY = block & 0xffe0;

				for (int x = 0; x < sizeX; x++)
				{
					for (int y = 0; y < sizeY; y++)
					{
						gfx.DrawImage(blocks, new Rectangle(posX + x * 8, posY + y * 8, 8, 8), blkX + (offset >> 2) * 8, blkY + (offset & 3) * 8, 8, 8, GraphicsUnit.Pixel);					
						offset++;
					}
				}
				ptr += 8;
			}
						
			gfx.Dispose();
			bmp.Save("out.png");

		}
	}
}


