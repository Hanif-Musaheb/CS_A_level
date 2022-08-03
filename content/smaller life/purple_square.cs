using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class purple_square : MonoBehaviour
{
    float timer;
    public SpriteRenderer purple_square_renderer;
 

    void Start()
    {
        float rand_color_factor = Random.Range(-0.1f, 0.1f);
        purple_square_renderer.material.color = new Vector4(255/255 + rand_color_factor, 255/255 + rand_color_factor, 255/255 + rand_color_factor, 1);//163, 121, 21
    }
    

    void Update()
    {
        //timer += Time.deltaTime;
        //if (timer > 2) {
        //    Destroy(this.gameObject);
        //}
    }
}
