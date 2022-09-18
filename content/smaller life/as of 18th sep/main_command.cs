using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class main_command : MonoBehaviour
{
    public GameObject food_prefab;
    public GameObject water_prefab;
    public GameObject basic_virus_prefab;

    Quaternion spawn_rotation = Quaternion.Euler(0, 0, 0);
    int random_scale;
    public float timer;
    public int wave=1;
    public bool playing;

    void Start()
    {
        

        for (int i = 0; i < 10; i++)
        {

            Vector2 spawn_location = new Vector2((Random.Range(-30,30) * .5f)-0.125f, (Random.Range(-30, 30) * .5f) - 0.125f);
            //print(spawn_location.x + ":" + spawn_location.y);
            var new_food = Instantiate(food_prefab, spawn_location, spawn_rotation, this.transform);
            random_scale = Random.Range(1,3);
            new_food.transform.localScale = new Vector2(random_scale, random_scale);
        }

        for (int i = 0; i < 5; i++)
        {
            Vector2 spawn_location = new Vector2((Random.Range(-30, 30) * .5f) - 0.125f, (Random.Range(-30, 30) * .5f) - 0.125f);
            //print(spawn_location.x + ":" + spawn_location.y);
            var new_food = Instantiate(water_prefab, spawn_location, spawn_rotation, this.transform);
            random_scale = Random.Range(3, 6);
            new_food.transform.localScale = new Vector2(random_scale, random_scale);
        }
    }

    void Update()
    {
        if (playing)
        {
            timer -= Time.deltaTime;
            if (timer < 0)
            {
                if (wave % 2 == 0)
                {
                    for (int i = 0; i < 10 * wave; i++)
                    {
                        float angle = Random.Range(0, 2 * Mathf.PI);
                        Vector2 spawn_location = new Vector2(25 * Mathf.Cos(angle), 25 * Mathf.Sin(angle));
                        Instantiate(basic_virus_prefab, spawn_location, spawn_rotation, this.transform);
                    }
                }
                timer = 10+wave;
                wave++;
            }
        }
    }
}

