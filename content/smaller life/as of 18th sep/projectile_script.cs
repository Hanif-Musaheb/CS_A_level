using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class projectile_script : MonoBehaviour
{
    public float damage = 25;
    public float speed;
    public string direction;
    public float time_to_death;
    float timer;
    List<string> obstacle_objects = new List<string>{ "food", "water" };

    Vector2 movement;


    void Start()
    {
        direction = set_direction();
        float x=0;
        float y=0;
        if (direction == "up")
        {
            x = 0;
            y = 1;
        }
        else if (direction == "down")
        {
            x = 0;
            y = -1;
        }

        else if (direction == "left")
        {
            x = -1;
            y = 0;
        }

        else if (direction == "right")
        {
            x = 1;
            y = 0;
        }

        movement = new Vector2(x, y);
    }
    void Update()
    {
        timer += Time.deltaTime;
        transform.Translate(movement*speed*Time.deltaTime);
        if (timer > time_to_death) {
            Destroy(this.gameObject);
            timer = 0;
        }
        
    }

    //void OnCollisionEnter2D(Collision2D collision)
    //{
    //    print("??????");
    //    if (collision.transform.tag == "virus")
    //    {

    //        Destroy(this.gameObject);
    //    }
    //}

    void OnTriggerEnter2D(Collider2D collision)
    {

        if (collision.transform.tag == "virus")
        {
            Destroy(collision.gameObject);
        }
        else if (obstacle_objects.Contains(collision.transform.tag)) { Destroy(this.gameObject); }
        
    }


    string set_direction()
    {
        return GetComponentInParent<attack_cell_script>().direction;
        
    }

}
