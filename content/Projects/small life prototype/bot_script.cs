using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bot_script : MonoBehaviour
{

    public float move_speed;
    Vector2 new_size;
    public float rotate_scope;
    float rand_rotation;
    public Object bot_prefab;
    Quaternion no_rotation = Quaternion.Euler(0, 0, 0);
    float split_threshold;


    public Color[] color_bank;
    int rand_num;
    public SpriteRenderer bot_renderer;



    void Start()
    {

        split_threshold = Random.Range(0.5f, 1f);

        SpriteRenderer parent_sprite_renderer = GetComponentInParent<SpriteRenderer>();
        
        if (parent_sprite_renderer.color!=Color.white)
        {
            print("boom");
            List<float> a = new List<float>(whiten_color(parent_sprite_renderer.color.r, parent_sprite_renderer.color.g, parent_sprite_renderer.color.b));
            Color parent_color = parent_sprite_renderer.color;
            //Color new_color = new Color(a[0], a[1], a[2], 1f);

            bot_renderer.color = parent_color;
            print("------");


        }
        else
        { 
            print("<><><><><>");
            bot_renderer = GetComponent<SpriteRenderer>();
            rand_num = Random.Range(0, color_bank.Length);
            bot_renderer.color = color_bank[rand_num];
        }




    }

    void Update()
    {
        rand_rotation += Random.Range(-rotate_scope, rotate_scope);
        //print(rand_rotation);
        Vector2 raw_movement = new Vector2(Mathf.Sin(rand_rotation), Mathf.Cos(rand_rotation));
        Vector2 movement = raw_movement * move_speed * Time.deltaTime;
        
        transform.Translate(movement);

        if (move_speed < 8) {
            move_speed += 0.1f;
        }


        if (transform.position.x > 11.125f + (transform.localScale.y / 2))
        {
            transform.Translate(new Vector2(-22.25f - transform.localScale.y, 0));
        }
        else if (transform.position.x < -11.125f - (transform.localScale.y / 2))
        {
            transform.Translate(new Vector2(22.25f + transform.localScale.y, 0));
        }


        if (transform.position.y > (5.5f + (transform.localScale.y / 2)))
        {
            transform.Translate(new Vector2(0, -10.5f - transform.localScale.y));

        }
        else if (transform.position.y < (-5.5f - (transform.localScale.y / 2)))
        {
            transform.Translate(new Vector2(0, 10.5f + transform.localScale.y));
        }

        if (transform.localScale.y >= split_threshold)
        {
            split();
        }

    }


    //private void split(){
    //    Vector3 bot_spawn_location = new Vector3(Random.Range(-10f, 10f), Random.Range(-5f, 5f));
    //    Instantiate(bot_prefab, bot_spawn_location, no_rotation);
    //}
    public List<float> whiten_color(float red,float green,float blue)
    {
        List<float> rgb = new List<float>();

        if (red == 1)
        {
            blue += 0.5f;
            green += 0.5f;
        }
        else if (blue == 1)
        {
            red += 0.5f;
            green += 0.5f;
        }
        else if (green == 1)
        {
            blue += 0.5f;
            red += 0.5f;
        }
        rgb.Add(red);
        rgb.Add(green);
        rgb.Add(blue);
        return rgb;
    }

    void split() {
        GameObject bot_child;
        bot_child = Instantiate(bot_prefab, new Vector2(transform.position.x + transform.localScale.x, transform.position.y), no_rotation) as GameObject;
        bot_child.transform.localScale = new Vector3(transform.localScale.x / 2.1f, transform.localScale.y / 2.1f, 1);
        transform.localScale = new Vector3(transform.localScale.x / 2.05f, transform.localScale.y / 2.05f, 1);

    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        Destroy(collision.gameObject);
        Vector2 current_size = transform.localScale;
        new_size = new Vector2(current_size.x + 0.01f, current_size.y + 0.01f);
        transform.localScale = new_size;
        move_speed = move_speed * 0.25f;  
    }
    
    void OnCollisionEnter2D(Collision2D collision)
    {
        SpriteRenderer collision_sprite_renderer = collision.gameObject.GetComponent<SpriteRenderer>();
        if (collision_sprite_renderer.color != bot_renderer.color)
        {
            if (((collision.gameObject.CompareTag("living")) || (collision.gameObject.CompareTag("Player")) || (collision.gameObject.CompareTag("plant"))) && (transform.localScale.x > collision.transform.localScale.x * 1.25f))
            {
                Vector2 current_size = transform.localScale;
                new_size = new Vector2(current_size.x + collision.transform.localScale.x / 4, current_size.y + collision.transform.localScale.x / 4);
                transform.localScale = new_size;
                Destroy(collision.gameObject);

            }
        }
    }
}
