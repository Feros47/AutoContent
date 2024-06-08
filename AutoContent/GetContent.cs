#nullable disable
namespace AutoContent;
using System.Diagnostics;

public class GetContent{
    
    private string result;
    public string run_cmd()
    {
        try
        {
            ProcessStartInfo start = new ProcessStartInfo
            {
                FileName = "python", 
                Arguments = "ChatgptPrompts.py", 
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true 
            };

            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result = reader.ReadToEnd();
                    Console.WriteLine(result);
                }

                using (StreamReader reader = process.StandardError)
                {
                    string error = reader.ReadToEnd();
                    if (!string.IsNullOrEmpty(error))
                    {
                        Console.WriteLine("Error: " + error);
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception: " + ex.Message);
        }
        return result;
    }
}