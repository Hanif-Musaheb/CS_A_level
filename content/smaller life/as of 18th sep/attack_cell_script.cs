using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class attack_cell_script : purple_square
{
    public string direction;
    public GameObject projectile_prefab;
    public float frequency; 

    float timer;

    bool[,] boarder_combinations ={

        {true,true,true,true},//surrounded0
        //single opening 
        {false,true,true,true},//right=r1
        {true,false,true,true},//left=l2
        {true,true,false,true},//up=u3
        {true,true,true,false},//down=d4
         //2 openings
        {false,false,true,true},//up down x5
        {true,true,false,false},//right left x6

        {true,false,false,true},//right down7
        {true,false,true,false},//right up8
        {false,true,true,false},//up left9
        {false,true,false,true},//up right10
        //3 openings
        {false,false,false,true},//down close (up)11
        {false,false,true,false},//up close (down)12
        {false,true,false,false},//left close (right)13
        {true,false,false,false}};//right close (left)14


    void Start()
    {
        Physics2D.queriesHitTriggers = true;
        Physics2D.queriesStartInColliders = false;
        boarder_check();
        Physics2D.queriesStartInColliders = true;
    }

    void boarder_check()
    {
        List<bool> boarder_contact = new List<bool>();
        boarder_contact.Add(hits_background_object(transform.right, 0.2f));
        boarder_contact.Add(hits_background_object(transform.right, -0.2f));
        boarder_contact.Add(hits_background_object(transform.up, 0.2f));
        boarder_contact.Add(hits_background_object(transform.up, -0.2f));
        //print(boarder_contact[0] + ""+boarder_contact[1] + "" + boarder_contact[2] + "" + boarder_contact[3]);

        List<string> possible_directions = new List<string> { "up", "down", "left", "right", "down", "up", "left", "right", "up" };

        if (same_order_check(boarder_contact, boarder_combination(0)))
        { Destroy(this.gameObject); }

        else if (same_order_check(boarder_contact, boarder_combination(1)))
        { direction="right"; }
        else if (same_order_check(boarder_contact, boarder_combination(2)))
        { direction = "left"; }
        else if (same_order_check(boarder_contact, boarder_combination(3)))
        { direction = "up"; }
        else if (same_order_check(boarder_contact, boarder_combination(4)))
        { direction = "down"; }

        else if (same_order_check(boarder_contact, boarder_combination(5)))
        { Destroy(this.gameObject); }
        else if (same_order_check(boarder_contact, boarder_combination(6)))
        { Destroy(this.gameObject); }

        else if (same_order_check(boarder_contact, boarder_combination(7)))
        { direction = possible_directions[Random.Range(5, 6)];}//up left
        else if (same_order_check(boarder_contact, boarder_combination(8)))
        { direction = possible_directions[Random.Range(1, 2)];  }//down left
        else if (same_order_check(boarder_contact, boarder_combination(9)))
        { direction = possible_directions[Random.Range(3, 4)];  }//down right
        else if (same_order_check(boarder_contact, boarder_combination(10)))
        { direction = possible_directions[Random.Range(7, 8)]; }//right up
        
        else if (same_order_check(boarder_contact, boarder_combination(11)))
        { direction = "up";  }
        else if (same_order_check(boarder_contact, boarder_combination(12)))
        { direction = "down"; }
        else if (same_order_check(boarder_contact, boarder_combination(13)))
        { direction = "right"; }
        else if (same_order_check(boarder_contact, boarder_combination(14)))
        { direction = "left"; }
    }

    List<bool> boarder_combination(int row)
    {
        List<bool> combination = new List<bool>();
        for (int i = 0; i < 4; i++) {
            combination.Add(boarder_combinations[row,i]);
        }
        return combination;
    }
    bool same_order_check(List<bool> list1, List<bool> list2)
        {
        for (int i = 0; i < 4; i++)
        {
            if (list1[i] != list2[i]) { return false; }
        }    
        return true;
    }

    bool hits_background_object(Vector2 direction, float distance)
    {
        RaycastHit2D hit_info = Physics2D.Raycast(transform.position, direction, distance);
        if (hit_info.collider != null)
        {
            return true;
        }     
        return false;
    }

    void Update()
    {
        timer += Time.deltaTime;
        if (timer > frequency)
        {
            Instantiate(projectile_prefab, transform.position, transform.rotation,this.transform);
            timer = 0;
            //var new_projectile_script = new_projectile.GetComponent<player_script>();
            //new_projectile_script.di
        }
    }

   
}
