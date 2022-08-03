using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player_script : main_command
{
    public float square_size;
    public Object stem_cell_prefab;
    Quaternion spawn_rotation = Quaternion.Euler(0, 0, 0);
    bool mouse_down = false;
    float timer;
    float square_distancing;
    public Vector2 spawn_location;
    public List<Vector2> player_cell_positions = new List<Vector2>();

    void Start()
    {
        square_distancing = 1 / square_size;
    }

    void Update()
    {



        Vector3 mouse_position = Input.mousePosition;
        spawn_location = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        spawn_location = new Vector2(Mathf.Round(spawn_location.x * square_distancing) / square_distancing, Mathf.Round(spawn_location.y * square_distancing) / square_distancing);


        if (Input.GetMouseButtonDown(0))
        {
            mouse_down = true;
        }
        //print(spawn_location.x + ":" + spawn_location.y);
        if (mouse_down && !(player_cell_positions.Contains(spawn_location)))
        {

            player_cell_positions.Add(spawn_location);
            Instantiate(stem_cell_prefab, spawn_location, spawn_rotation, this.transform);

        }
        if (Input.GetMouseButtonUp(0))
        {
            mouse_down = false;
        }


        if (Input.GetMouseButtonDown(0))
        {
            Debug.Log("Pressed left click, casting ray.");
            CastRay();
        }

    }

    void CastRay()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit2D hit = Physics2D.Raycast(ray.origin, ray.direction, Mathf.Infinity);
        if (hit.collider != null&&hit.collider.tag=="food")
        {
            Debug.Log(hit.collider.gameObject.name);
        }
    }
        

}
