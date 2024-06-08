namespace AutoContent;

public class Sampler
{
    private string gptContent;
    public Sampler() {
        gptContent = "";
    }
    private string GetChatGPTContent() {
        GetContent content = new GetContent();
        return content.run_cmd();
    }
    public void Sample() {
        gptContent = GetChatGPTContent();
    }
}
