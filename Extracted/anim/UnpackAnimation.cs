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

			//uint addr = 0x0;
			//uint ptr = addr & 0xffffff;
			uint ptr = 0x7e754;

			int count = data[ptr];
			Console.WriteLine("count: {0}", count);
			ptr +=2;

			int posX=0, posY=0;
			Console.WriteLine("posX: {0} posY: {1}", posX, posY);

			for (int s = 0; s < count; s++)
			{
				if (s == 0)
				{
					posX = 256 + (sbyte)data[ptr];
					posY = 256 + (sbyte)data[ptr] + 1;
					Console.WriteLine("posX: {0} posY: {1}", posX, posY);
				}
				else
				{
					posX += (sbyte)data[ptr];
					posY += (sbyte)data[ptr + 1];
					Console.WriteLine("posX: {0} posY: {1}", posX, posY);
				}
				int sizeX = ((data[ptr + 2] & 0xf) >> 2) +1;
				Console.WriteLine("sizeX: {0}", sizeX);
				int sizeY = (data[ptr + 2] & 0x3) +1;
				Console.WriteLine("sizeY: {0}", sizeY);
				int offset = data[ptr+7];
				Console.WriteLine("offset: {0}", offset);
				int block = (data[ptr +4] << 8) + data[ptr + 5];
				Console.WriteLine("block: {0}", block);

				int blkX = (block & 0x1f) << 5;
				Console.WriteLine("blkX: {0}", blkX);
				int blkY = block & 0xffe0;
				Console.WriteLine("blkY: {0}", blkY);

				for (int x = 0; x < sizeX; x++)
				{
					for (int y = 0; y < sizeY; y++)
					{
						Console.WriteLine("count: {0} {1}", sizeX, sizeY);
						gfx.DrawImage(blocks, new Rectangle(posX + x * 8, posY + y * 8, 8, 8), blkX + (offset >> 2) * 8, blkY + (offset & 3) * 8, 8, 8, GraphicsUnit.Pixel);					
						offset++;
					}
				}
				ptr += 8;
			}
						
			gfx.Dispose();
			bmp.Save(string.Format(@"out_0x{0}{1}.png", posX, posY));

		}
	}
}


