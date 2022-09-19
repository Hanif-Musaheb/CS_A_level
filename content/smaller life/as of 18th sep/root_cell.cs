using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class root_cell : purple_square 
{
    float timer;
    
    void Start()
    {
        float rand_color_factor = Random.Range(-0.1f, 0.1f);
        purple_square_renderer.material.color = new Vector4(255 / 255 + rand_color_factor, 255 / 255 + rand_color_factor, 255 / 255 + rand_color_factor, 1);//163, 121, 21


        Physics2D.queriesHitTriggers = true;
        Physics2D.queriesStartInColliders = false;
        if (!attached() && this.transform.tag != "nucleus") { Destroy(this.gameObject); }
        Physics2D.queriesStartInColliders = true;
    }

    void Update()
    {
        timer += Time.deltaTime;
        if (timer > 5)//optimisation measure
        {
            Physics2D.queriesStartInColliders = false;
            boarder_check();
            Physics2D.queriesStartInColliders = true;
            timer = 0;
        }
        Physics2D.queriesStartInColliders = true;
        if (health <= 0) { Destroy(this.gameObject); }
    }

    void boarder_check() {
        hits_background_object(transform.right, 0.2f);
        hits_background_object(transform.right, -0.2f);
        hits_background_object(transform.up, 0.2f);
        hits_background_object(transform.up, -0.2f);
    }

    void hits_background_object(Vector2 direction, float distance)
    {
        RaycastHit2D hit_info = Physics2D.Raycast(transform.position, direction, distance);
        //print("!!!");
        if (hit_info != false)
        {
            //print(hit_info.collider.tag);

            if (hit_info.collider.tag == "food")
            {
                this.tag = "root_f";
                

            }
            else if (hit_info.collider.tag == "water")
            {
                this.tag = "root_w";
            }
        }
    }
}
