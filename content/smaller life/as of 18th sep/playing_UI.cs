using UnityEngine;
using UnityEngine.UI;

public class playing_UI : MonoBehaviour 
{
    public Text water_text;
    public Text energy_text;
    

    public void update_energy(float total_energy)
    {
        energy_text.text = Mathf.Round(total_energy).ToString()+"µJ";

    }

    public void update_water_percentage(float water_percentage)
    {
        if (water_percentage > 1) { water_percentage = 1; }
        water_text.text = Mathf.Round(water_percentage*100).ToString() + "%";

    }

}
