using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JIB : MonoBehaviour
{
    public float move_speed;
    Vector2 new_size;
    public Camera cam;

    void Update()
    {
        Vector2 raw_movement = new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical"));
        Vector2 movement = raw_movement * move_speed * Time.deltaTime;
        transform.Translate(movement);

        if (transform.position.x > 11.125f+ (transform.localScale.y / 2)) { 
            transform.Translate(new Vector2(-22.25f - transform.localScale.y, 0));
        }
        else if (transform.position.x < -11.125f-(transform.localScale.y / 2)) {
            transform.Translate(new Vector2(22.25f + transform.localScale.y, 0));
        }



        if (transform.position.y > (5.5f + (transform.localScale.y/2))) {
            transform.Translate(new Vector2(0, -10.5f-transform.localScale.y ));
        
        }
        else if (transform.position.y < (-5.5f - (transform.localScale.y / 2))) {
            transform.Translate(new Vector2(0, 10.5f + transform.localScale.y));
        }

        //print((Screen.height/80f) + "," + (Screen.width/80f));
        //400,850 10.625,5
        //float width = 1 / (cam.WorldToViewportPoint(new Vector3(1, 1, 0)).x - .5f);
        //print(width);

    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (transform.localScale.y >= 9)
        {
            print("max size reached");
        }
        else
        {
            print(collision);
            Destroy(collision.gameObject);
            print(transform.localScale);
            Vector2 current_size = transform.localScale;
            new_size = new Vector2(current_size.x + 0.05f, current_size.y + 0.05f);
            transform.localScale = new_size;
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (((collision.gameObject.CompareTag("living")) || (collision.gameObject.CompareTag("plant"))) && (transform.localScale.x>collision.transform.localScale.x*1.25f))
            {
            print("eat"+ transform.localScale.x * 1.1f );
            Vector2 current_size = transform.localScale;
            new_size = new Vector2(current_size.x + collision.transform.localScale.x/16, current_size.y + collision.transform.localScale.x/16);
            transform.localScale = new_size;
            Destroy(collision.gameObject);
           
        }
    }
}
