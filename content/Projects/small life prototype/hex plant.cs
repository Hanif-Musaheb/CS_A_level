using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class hex_plant : MonoBehaviour
{
    public Object plant_prefab;
    float timer = 0;
    float second_timer = 0;
    float third_timer = 0;
    float timer_max = 8;
    List<int> boarder_direction = new List<int> {0,60,120,180,240,300};

    bool locked=false;
    public int c=5;
    public int current_direction = 0;
    public List<int> free_boarders = new List<int> { };
    Quaternion spawn_rotation = Quaternion.Euler(0, 0, 0);

    public Renderer plant_renderer;
    

    void Start()
    {
        if ((transform.position.x > 9) || (transform.position.x < -9) || (transform.position.y < -4) || (transform.position.y > 4))
        {
            DestroyObject(gameObject);

        }
        timer_max = Random.Range(4f, 10f);
        transform.localScale = new Vector3(0.05f, 0.05f, 1f);

        Physics2D.queriesHitTriggers = true;
        Physics2D.queriesStartInColliders = false;
    }

    void Update()
    { 

    }

    void FixedUpdate()
    {
        if (!locked)
        {
            second_timer += Time.deltaTime;
            if ((transform.localScale.x < 0.124f) && (second_timer > 0.005f))
            {
                second_timer = 0;
                Vector2 plant_scale = new Vector2(transform.localScale.x + 0.001f, transform.localScale.y + 0.001f);
                transform.localScale = plant_scale;
            }
            else
            {
                transform.localScale = new Vector3(0.125f, 0.125f, 0);
            }
            timer += Time.deltaTime;
            if ((timer > timer_max) && (transform.localScale.x > 0.1f))
            {
                replicate();
            }
        }
       
    }

    List<int> boarders_check()
    {
        free_boarders = new List<int> { };
        while (true)
        {
            third_timer += Time.deltaTime;
            if (third_timer > 0.2f)
            {
                third_timer = 0;
                transform.Rotate(new Vector3(0, 0, 60));
                current_direction++;
                if (current_direction >= 6)
                {
                    current_direction = 0;
                    return free_boarders;
                }


                RaycastHit2D hit_info = Physics2D.Raycast(transform.position, transform.right, 0.4f);
                if (hit_info.collider != null)
                {
                    //Debug.DrawLine(transform.position, hit_info.point, Color.red);

                }
                else
                {
                    //Debug.DrawLine(transform.position, transform.position + transform.right * 10, Color.green);
                    free_boarders.Add(current_direction);
                }
            }
            
        }

    }

    void replicate()
    {
        List<int> free_boarders = boarders_check();
        if (free_boarders.Count > 0)
        {
            timer = 0;
            //float radius = Mathf.Sqrt(Mathf.Pow(transform.localScale.x, 2) + Mathf.Pow(transform.localScale.y, 2));
            float radius = 0.125f;
            int rand_num = Random.Range(0, free_boarders.Count);
            float direction = (boarder_direction[free_boarders[rand_num]]) * Mathf.Deg2Rad;
            float rand_boarder_x = Mathf.Cos(direction) * radius;
            float rand_boarder_y = Mathf.Sin(direction) * radius;
            Instantiate(plant_prefab, new Vector2(rand_boarder_x + transform.position.x, rand_boarder_y + transform.position.y), spawn_rotation);
            
        }
        else {
            float rand_color_factor = Random.Range(-0.1f, 0.1f);
            plant_renderer.material.color = new Vector4(0.64f+ rand_color_factor, 0.47f+ rand_color_factor, 0.01f+ rand_color_factor, 1);//163, 121, 21
            locked = true;
        }

    }



}
