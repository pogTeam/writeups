# shamecontrol

## Description
[EN]
What if it is a Windows .exe, do you still can? 
Flag format: "3DS{flag}" 

[PT-BR]
E se for binario Windows, voce ainda consegue? 
Flag no formato: "3DS{flag}" 

## Solution

Another .NET application, but this time there was no output when we tried to run the application in console mode. So, let's read the code:

```csharp
namespace ConsoleApplication2
{
	// Token: 0x02000002 RID: 2
	internal class Program
	{
		// Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
		private static void Main(string[] args)
		{
			string text = "40";
			RegistryKey currentUser = Registry.CurrentUser;
			if (Debugger.IsAttached)
			{
				Console.WriteLine("3DS{2}j{0}t{0}v{0}c{0}b{0}nd{1}{3}", new object[]
				{
					text[1],
					text[0],
					"{",
					"}"
				});
			}
			RegistryKey registryKey = currentUser.OpenSubKey("parangaricutirimirruaro");
			if (registryKey != null)
			{
				Console.WriteLine("3DS{2}j{0}t{0}v{0}c{0}b{0}nd{1}{3}", new object[]
				{
					text[0],
					text[1],
					"{",
					"}"
				});
				registryKey.Close();
			}
			currentUser.Close();
		}
	}
}
```

A simple substitution on the given string was enough to get the solution. But there was some debugger verification on the code:

```csharp
if (Debugger.IsAttached)
```

This generates a fake flag: 3DS{j0t0v0c0b0nd4}

The vector starts from zero, so the correct approach:
```
text[0] = 4 
text[1] = 0
```

Flag: 3DS{j4t4v4c4b4nd0}
