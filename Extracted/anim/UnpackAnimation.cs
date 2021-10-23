// Code by Hpman 

// $ mcs -out:UnpackAnimation.exe UnpackAnimation.cs

using System;
using System.IO;

namespace UnpackAnimation {
	class Decode {
		static void Main(string[] args) {
			Console.WriteLine("Reading packed animation data!");

			byte[] animData;
			animData = File.ReadAllBytes(@"unpk_0x0c0000.bin");


		}
	}
}


