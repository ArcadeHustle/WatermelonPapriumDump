// Code by Hpman 

// $ mcs -out:UnpackAnimation.exe UnpackAnimation.cs -r:System.Drawing.dll 

using System;
using System.IO;
using System.Drawing;

namespace UnpackAnimation {
	class Decode {
		static void Main(string[] args) {
			Console.WriteLine("Reading packed animation data!");

			byte[] animData;
			animData = File.ReadAllBytes(@"unpk_0x0c0000.bin");

			Bitmap bmp = new Bitmap(512,512);
			bmp.MakeTransparent();
			Graphics gfx = Graphics.FromImage(bmp);

			// https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.drawimage?view=windowsdesktop-5.0#System_Drawing_Graphics_DrawImage_System_Drawing_Image_System_Drawing_Rectangle_System_Single_System_Single_System_Single_System_Single_System_Drawing_GraphicsUnit_System_Drawing_Imaging_ImageAttributes_
			//gfx.DrawImage()
		
			bmp.Save("out.png");

		}
	}
}


