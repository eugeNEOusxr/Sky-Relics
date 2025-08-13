using UnityEngine;

public class TestScript : MonoBehaviour
{
    void Start()
    {
        Debug.Log("Hello from Unity!");
    }

    void Update()
    {
        // This will log the frame count each second.
        if (Time.frameCount % 60 == 0)
        {
            Debug.Log($"Frame: {Time.frameCount}");
        }
    }
}
