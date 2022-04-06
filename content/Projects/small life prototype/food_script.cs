using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class food_script : MonoBehaviour
{
    public Object plant_prefab;
    float timer = 0;
    float second_timer = 0;
    float timer_max=8;
    float a;

    Quaternion spawn_rotation = Quaternion.Euler(0, 0, 0);

    void Start()
    {
        if ((transform.position.x>9)|| (transform.position.x < -9)|| (transform.position.y < -4) || (transform.position.y > 4))
        {
            DestroyObject(gameObject);

        }
                timer_max = Random.Range(4f, 10f);
        transform.localScale = new Vector3(0.05f, 0.05f, 1f);

    }

    void Update()
    {
        //Vector3 rotation = new Vector3(0, 0, 1);
        //transform.Rotate(rotation); 
    }

    void FixedUpdate()
    {
        //print(timer_max);
        second_timer += Time.deltaTime;
        if ((transform.localScale.x < 0.125f) && (second_timer > 0.1f))
        {
            second_timer = 0;
            Vector2 plant_scale = new Vector2(transform.localScale.x + 0.01f, transform.localScale.y + 0.01f);
            transform.localScale = plant_scale;
        }

        timer += Time.deltaTime;
        if ((timer > timer_max) && (transform.localScale.x > 0.1f))
        {
            timer = 0;
            float rand_offset = Random.Range(0f, 180f);
            Vector2 spawn_offset = new Vector2(Mathf.Sin(rand_offset), Mathf.Cos(rand_offset));
            spawn_offset = spawn_offset * Random.Range(0f, 1f);
            Instantiate(plant_prefab, new Vector2(transform.position.x + spawn_offset.x, transform.position.y + spawn_offset.y), spawn_rotation);
        }
    }
}
