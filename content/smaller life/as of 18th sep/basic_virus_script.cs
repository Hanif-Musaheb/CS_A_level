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

    Vector3 targetPos = new Vector3(0, 0, 0);
    bool obstacle_infront = false;
    public float timer = 0;
    float obstacle_size;
    public float angle;

    bool avoid_right;
    public Vector3 direction;

    void Start()//function run at start
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

        bool avoid_right = Random.value > 0.5;
    }

    void Update()//function run every frame
    {

        timer += Time.deltaTime;
        //nucleus targeting
        targetPos.x = nucleus_position.x - transform.position.x;
        targetPos.y = nucleus_position.y - transform.position.y;
        angle = Mathf.Atan2(targetPos.y, targetPos.x) * Mathf.Rad2Deg;


        Physics2D.queriesStartInColliders = false;
        RaycastHit2D hit_info = Physics2D.Raycast(transform.position, direction, Mathf.Infinity);
        Physics2D.queriesStartInColliders = true;


        //obstacle avoidance
        if (hit_info != false)
        {
            print("!!!");
            if (hit_info.collider.tag == "water" || hit_info.collider.tag == "food")
            {
                print("not insight");
                if (avoid_right)
                {
                    transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle + 90));
                    direction = -transform.up;
                }
                else
                {
                    transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle - 90));
                    direction = transform.up;
                }

            }
        }
        else
        {
            print("insight");
            transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle));
            direction = transform.right;
        }

        Debug.DrawRay(transform.position, direction*5, Color.green);


        //movement
        transform.Translate(speed * Time.deltaTime, 0, 0);

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
//    Physics2D.queriesStartInColliders = false;
//        RaycastHit2D hit_info = Physics2D.Raycast(transform.position, nucleus_position, Mathf.Infinity);
//    Physics2D.queriesStartInColliders = true;


//        //obstacle avoidance

//        if (hit_info.collider.tag == "water" || hit_info.collider.tag == "food") {
//            print("not insight");
//    //if (avoid_right) { transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle + 90)); }
//    //else { transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle-90)); }

//}
//        else
//{
//    print("insight");
//    //transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle));
//}

//Debug.DrawRay(transform.position, nucleus_position, Color.green);


//transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle));


//bool obstacle_avoidance(Vector3 direction) {
//    Physics2D.queriesStartInColliders = false;
//    RaycastHit2D hit_info = Physics2D.Raycast(transform.position, direction, 3);
//    Physics2D.queriesStartInColliders = true;
//    if (hit_info != false)
//    {
//        if (hit_info.collider.tag == "water" || hit_info.collider.tag == "food")
//        {
//            return true;
//        }
//    }
//    return false;

//}


//if (hit_info != false)
//{
//    if (hit_info.collider.tag == "water" || hit_info.collider.tag == "food")
//    {
//        if (hit_info.distance < 0.1f) { timer = 0; }
//    }
//}
//if (timer < 5 && (Vector2.Angle(hit_info.normal, transform.right) < 2 || Vector2.Angle(hit_info.normal, transform.right) > 2))
//{ transform.rotation = Quaternion.Euler(new Vector3(0, 0,angle+ 90)); }

//if (timer < 2.5f)
//{ transform.rotation = Quaternion.Euler(new Vector3(0, 0, Vector2.Angle(hit_info.normal, transform.right))); }

//else
//{transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle));}

//obstacle avoidance

//List<bool> rays_detected = new List<bool> { };
//rays_detected.Add(obstacle_avoidance(new Vector3(transform.right.x, transform.right.y, transform.right.z) * 2.8f));
//rays_detected.Add(obstacle_avoidance(new Vector3((transform.up.x + transform.right.x * 4) / 5, (transform.up.y + transform.right.y * 4) / 5, transform.up.z) * 3.5f));
//rays_detected.Add(obstacle_avoidance(new Vector3((-transform.up.x + transform.right.x * 4) / 5, (-transform.up.y + transform.right.y * 4) / 5, transform.up.z) * 3.5f));

////if (obstacle_avoidance_offset > 3) { obstacle_avoidance_offset -= Time.deltaTime*5; }
////else { obstacle_avoidance_offset = 0; };

//if (!rays_detected.Contains(true)) {
//    obstacle_avoidance_offset = 0;
//    transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle + obstacle_avoidance_offset));
//}
//else {
//     if (rays_detected[0] == true || rays_detected[2] == true)
//    { }
//    else if (rays_detected[1] == true && (rays_detected[0] == true || rays_detected[2] == true))
//    {
//        if (rays_detected[0] == true)
//        { obstacle_avoidance_offset += 2; }

//        else if (rays_detected[2] == true)
//        { obstacle_avoidance_offset -= 2; }
//    }
//    else { obstacle_avoidance_offset += 5; }
//    transform.rotation = Quaternion.Euler(new Vector3(0, 0, angle + obstacle_avoidance_offset));
////}
////left middle right
//print(rays_detected[0] + ":" + rays_detected[1] + ":" + rays_detected[2]);



//print(obstacle_infront);





//    float obstacle_avoidance(Vector3 direction) {
//        Physics2D.queriesStartInColliders = false;
//        RaycastHit2D hit_info = Physics2D.Raycast(transform.position, direction, 2);
//        Physics2D.queriesStartInColliders = true;
//        if (hit_info != false)
//        {
//            if (hit_info.collider.tag == "water" || hit_info.collider.tag == "food")
//            {
//                print("!!");
//                if (hit_info.distance < b) {
////                    print(direction);

//                    if (direction == transform.up) { obstacle_avoidance_offset += a; print("left"); }
//                    else if (direction == -transform.up) { obstacle_avoidance_offset -= a; print("right"); }
//                    else if (direction == transform.right) { obstacle_avoidance_offset +=Random.Range(-1,1)*90 ; print("forward"); }
//                }
//            }
////        }
////        return obstacle_avoidance_offset;
//    }

















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


//timer += Time.deltaTime;
//if (timer >= obstacle_size * 1.25f) { obstacle_infront = false; }



//targetPos.x = nucleus_position.x - transform.position.x;
//targetPos.y = nucleus_position.y - transform.position.y;
//angle = Mathf.Atan2(targetPos.y, targetPos.x) * Mathf.Rad2Deg;

////obstacle avoidance
//Physics2D.queriesStartInColliders = false;
//RaycastHit2D hit_info = Physics2D.Raycast(transform.position, transform.right, 2);
//Physics2D.queriesStartInColliders = true;

//print(obstacle_infront);

//Debug.DrawRay(transform.position, transform.right, Color.green);
//Debug.DrawRay(transform.position, transform.up, Color.green);
//Debug.DrawRay(transform.position, -transform.up, Color.green);

//if (hit_info != false)
//{
//    if (hit_info.collider.tag == "water" || hit_info.collider.tag == "food")
//    {
//        obstacle_infront = true;
//        obstacle_size = hit_info.transform.lossyScale.x;
//        timer = 0;

//        //angle = transform.rotation.eulerAngles.z + Random.Range(30, 60);
//    }
//}

//if (obstacle_infront) { angle +=  (Mathf.Cos(timer / obstacle_size * 1.25f) * 90); }
