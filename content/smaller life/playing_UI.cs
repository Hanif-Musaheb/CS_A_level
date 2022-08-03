using UnityEngine;
using UnityEngine.UI;

public class playing_UI : player_script 
{
    public Text water_text;
    public Text energy_text;

    float timer;

    void Update()
    {
        timer += Time.deltaTime;
        energy_text.text = timer.ToString();
    }
}
