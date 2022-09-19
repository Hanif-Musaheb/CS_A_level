using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class basic_virus_script : MonoBehaviour
{
    Vector3 nucleus_position;
    float speed;
    public float health;
    float damage;
    public List<string> cell_types;

    float[] health_probabilities = { 50, 150 };
    float[] speed_probabilities = { 1f, 2f };
    float[] damage_probabilities = { 50f };

    void Start()
    {
        health = Random.Range(health_probabilities[0], health_probabilities[1]);
        speed = Random.Range(speed_probabilities[0], speed_probabilities[1]);
        damage = damage_probabilities[0];

        var nucleus = GameObject.FindGameObjectsWithTag("nucleus");
        if (nucleus.Length > 0)
        {
            nucleus_position = nucleus[0].transform.position;
        }
        else { print("no nucleus"); }
    }

    void Update()
    {
        Vector3 targetPos = new Vector3(0, 0, 0);
        //movement
        targetPos.x = nucleus_position.x - transform.position.x;
        targetPos.y = nucleus_position.y - transform.position.y;
        float angle = Mathf.Atan2(targetPos.y, targetPos.x) * Mathf.Rad2Deg;
        transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle));
        transform.Translate(speed * Time.deltaTime, 0, 0);


        //raycast
        //Debug.DrawRay(transform.position, transform.TransformDirection(Vector2.right) * 0.18f, Color.red);

        //RaycastHit2D hit_info = Physics2D.Raycast(transform.position, transform.TransformDirection(Vector2.right), 0.18f);//new Vector2(nucleus_position.x,nucleus_position.y), 1f);

        //if (hit_info)
        //{
        //    if (cell_types.Contains(hit_info.collider.tag))
        //    {
        //        try
        //        {
        //            var hit_info_script = hit_info.collider.GetComponent<purple_square>();
        //            hit_info_script.update_health(damage);
        //            Destroy(this.gameObject);
        //        }
        //        catch(System.Exception e) {
        //            var hit_info_script = hit_info.collider.GetComponent<projectile_script>();
        //            health -= hit_info_script.damage;
        //            Destroy(hit_info.collider.gameObject); 

        //         }

        //    }
        //}


        if (health < 0) { Destroy(this.gameObject); }
    }
    public void update_health(float damage) { health -= damage; }

    void OnTriggerEnter2D(Collider2D collision)
    {
        if (cell_types.Contains(collision.tag))
        {
            var script_of_collision = collision.gameObject.GetComponent<purple_square>();
            print("the other one");
            script_of_collision.update_health(damage);
            Destroy(this.gameObject);




        }
        else if (collision.tag == "projectile")
        {

            var script_of_collision = collision.gameObject.GetComponent<projectile_script>();
            print("projectile" + script_of_collision.damage);
            health -= script_of_collision.damage;
            Destroy(collision.gameObject);
        }
    }
}
