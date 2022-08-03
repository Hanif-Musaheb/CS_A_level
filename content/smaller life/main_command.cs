using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class main_command : MonoBehaviour
{
    public GameObject food_prefab;
    public GameObject water_prefab;

    Quaternion spawn_rotation = Quaternion.Euler(0, 0, 0);
    int random_scale;
    public List<Vector2> material_positions = new List<Vector2>();


    void Start()
    {
        

        for (int i = 0; i < 1; i++)
        {

            Vector2 spawn_location = new Vector2((Random.Range(-9,9) * .5f)-0.125f, (Random.Range(-9, 9) * .5f) - 0.125f);
            //print(spawn_location.x + ":" + spawn_location.y);
            var new_food = Instantiate(food_prefab, spawn_location, spawn_rotation, this.transform);
            random_scale = Random.Range(1,3);

            material_position_finder(spawn_location, random_scale);
            
            new_food.transform.localScale = new Vector2(random_scale,random_scale);

        }

        //for (int i = 0; i < 5; i++)
        //{
        //    Vector2 spawn_location = new Vector2((Random.Range(-30, 30) * .5f) - 0.125f, (Random.Range(-30, 30) * .5f) - 0.125f);
        //    print(spawn_location.x + ":" + spawn_location.y);
        //    var new_food = Instantiate(water_prefab, spawn_location, spawn_rotation, this.transform);
        //    random_scale = Random.Range(3, 10) * .5f;
        //    new_food.transform.localScale = new Vector2(random_scale, random_scale);
        //}





    }

    private List<Vector2> material_position_finder(Vector2 raw_position,int size) {
        raw_position = new Vector2(raw_position.x - 0.125f, raw_position.y - 0.125f);
        //List<Vector2> material_positions = new List<Vector2>();
        for (int i = 0; i < size - 1; i++)
        {
            for(int j =0; i < size - 1; i++)
            {
                material_positions.Add(new Vector2(raw_position.x + (0.25f * i)-0.25f*size, raw_position.y + (0.25f * j)));

            }
        }
        material_positions.Add(new Vector2(raw_position.x , raw_position.y));
        print("????");
        
        return material_positions;

    }


}

