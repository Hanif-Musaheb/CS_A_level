using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player_script : main_command
{
    bool mouse_down = false;
    float timer;
    float square_distancing;
    public float square_size;
    Vector2 nucleus_location;
    bool nucleus_placed = false;
    Object nucleus;
    float camera_speed=0.05f;
    float time=0;
    float light_level;
    float total_energy;

    public float water_need;
    float water_percentage;

    public Vector2 spawn_location;
    public Vector3 mouse_position;
    Quaternion spawn_rotation = Quaternion.Euler(0, 0, 0);

    public Object stem_cell_prefab;
    public Object root_cell_prefab;
    public Object nucleus_prefab;
    public Object chloroplast_prefab;
    public Object attack_cell_prefab;
    public Object wall_cell_prefab;
    Object cell_type_selected;

    playing_UI playing_UI;

   

    void Start()
    {
        square_distancing = 1 / square_size;
        cell_type_selected = stem_cell_prefab;
        nucleus = Instantiate(nucleus_prefab, new Vector2(0,0), spawn_rotation, this.transform);
        playing_UI = GameObject.FindObjectOfType<playing_UI>();

    }

    void Update()
    {
        //Camera.main.transform.position = new Vector3(spawn_location.x, spawn_location.y, -10);
        total_energy += photosynthetic_energy()+food_energy();
        playing_UI.update_energy(total_energy);
        playing_UI.update_water_percentage(water_percentage_calculator());//optimisable

        time += Time.deltaTime;
       
        
        light_level = (Mathf.Sin(time/20) + 1)/2;//yellow tint:::
        Camera.main.backgroundColor = new Vector4(light_level, light_level, light_level, 1);
        Camera.main.transform.position = new Vector3(Camera.main.transform.position.x+(Input.GetAxis("Horizontal")*camera_speed), Camera.main.transform.position.y + (Input.GetAxis("Vertical") * camera_speed), -10);


        mouse_position = Input.mousePosition;
        spawn_location = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        spawn_location = new Vector2(Mathf.Round(spawn_location.x * square_distancing) / square_distancing, Mathf.Round(spawn_location.y * square_distancing) / square_distancing);




        if (Input.GetMouseButtonDown(0))
        {
            mouse_down = true;
        }
        if (mouse_down)
        {
            if (!CastRay()&& 75<mouse_position.y)//could be more specific,might not work with all computer configurations::::
            {
                if (cell_type_selected == nucleus_prefab)
                {
                    Destroy(nucleus);
                    nucleus = Instantiate(nucleus_prefab, spawn_location, spawn_rotation, this.transform);
                }
                else
                {
                    Instantiate(cell_type_selected, spawn_location, spawn_rotation, this.transform);
                }
            }
        }
        if (Input.GetMouseButtonUp(0))
        {
            mouse_down = false;
        }

        if (Input.GetMouseButtonDown(0))
        {
            //Debug.Log("Pressed left click, casting ray.");
            CastRay();
        }
        water_percentage_calculator();
        //print(water_percentage_calculator());
    }



    float water_percentage_calculator()
    {

        var roots_with_water = GameObject.FindGameObjectsWithTag("root_w");
        var roots_with_food = GameObject.FindGameObjectsWithTag("root_f");
        var chloroplasts = GameObject.FindGameObjectsWithTag("chloroplast");

        //sprint( "water:" + roots_with_water.Length+ "   food:" + roots_with_food.Length  + "  chloroplasts:"+ chloroplasts.Length);

        water_need = roots_with_food.Length * .5f + (chloroplasts.Length * 0.8f * light_level);


        if (water_need == 0)
        {
            water_percentage = 0;
            return water_percentage;
        }
        water_percentage = roots_with_water.Length / water_need;
        return water_percentage;

    }

    public float food_energy()
    {
        var roots_with_food = GameObject.FindGameObjectsWithTag("root_f");
        float water_factor;
        if (water_percentage_calculator() > 1) { water_factor = 1; }
        else { water_factor = water_percentage_calculator(); }
        float energy = roots_with_food.Length * 0.8f * Time.deltaTime * water_factor;
        //print(energy+":food energy");
        return energy;
    }

    public float photosynthetic_energy()
    {
        var chloroplasts = GameObject.FindGameObjectsWithTag("chloroplast");
        float water_factor;
        if (water_percentage_calculator() > 1) { water_factor = 1; }
        else { water_factor = water_percentage_calculator(); };
        float energy = chloroplasts.Length * 0.2f *light_level* Time.deltaTime*water_factor;
        
        return energy;
    }

    bool CastRay()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit2D hit = Physics2D.Raycast(ray.origin, ray.direction, Mathf.Infinity);
        if (hit.collider != null)
        {
            //Debug.Log(hit.collider.gameObject.name);
            return true;
        }
        return false;
    }

    public void basic_cell_press()
    {
        cell_type_selected = stem_cell_prefab;
    }

    public void root_cell_press()
    {
        cell_type_selected = root_cell_prefab;
    }

    public void nucleus_press()
    {
        cell_type_selected = nucleus_prefab;
    }

    public void chloroplast_press()
    {
        cell_type_selected = chloroplast_prefab;
    }

    public void attack_cell_press()
    {
        cell_type_selected = attack_cell_prefab;
    }
    public void wall_cell_press()
    {
        cell_type_selected = wall_cell_prefab;
    }
    //when you have free time but arent focused complete the button press and tag things
}
