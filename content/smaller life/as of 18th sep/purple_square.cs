using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class purple_square : MonoBehaviour
{
    float timer;
    public SpriteRenderer purple_square_renderer;
    public List<string> cell_types;
    public float health;

    void Start()
    {
       
        float rand_color_factor = Random.Range(-0.1f, 0.1f);
        purple_square_renderer.material.color = new Vector4(255/255 + rand_color_factor, 255/255 + rand_color_factor, 255/255 + rand_color_factor, 1);//163, 121, 21

        
        Physics2D.queriesHitTriggers = true;
        Physics2D.queriesStartInColliders = false;
        if (!attached()&&this.transform.tag!="nucleus") { Destroy(this.gameObject); }
        Physics2D.queriesStartInColliders = true;

    }

    void Update()
    {
        if (health <= 0) { Destroy(this.gameObject); }   
    }

    public bool attached()
    {
        List<bool> boarder_contact = new List<bool>();

        boarder_contact.Add(hits_player_cell(transform.right, 0.2f));
        boarder_contact.Add(hits_player_cell(transform.right, -0.2f));
        boarder_contact.Add(hits_player_cell(transform.up, 0.2f));
        boarder_contact.Add(hits_player_cell(transform.up, -0.2f));
        //print(boarder_contact[0]+""+ boarder_contact[1]+ boarder_contact[2]+ boarder_contact[3]);
        if (boarder_contact.Contains(true)) { return true; }
        return false;

    }

    bool hits_player_cell(Vector2 direction, float distance)
    {
        RaycastHit2D hit_info = Physics2D.Raycast(transform.position, direction, distance);
        if (hit_info.collider != null)
        {
            if (cell_types.Contains(hit_info.transform.tag))
            {
                //print(hit_info.collider.name);
                return true;
            }
        }
        return false;
    }

    public void update_health(float damage)
    {
        health -= damage;
    }

}
//bug with the cell types didnt add new root cell types that i added 
