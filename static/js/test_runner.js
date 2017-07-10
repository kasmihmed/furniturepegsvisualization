/**
 * Created by sidik on 5/1/17.
 */

function select_element(element_id)
{
    console.log(element_id);
    if (element_id == "slider-bottom-right-button"){
        if ($("#slider-bottom-right-button").children()[0].getAttribute('src')==""){
           console.log('done with lower slider') ;
        }
        else{
            get_next_pegs('canvas');
        }
    }
    else{
        $("#"+element_id).click();
    }

}

var furniture_index = 0;
var peg_index = 0;
var slider_reverse_elements=6;
function furniture_selection_loop() {
    var slider_action=0
    peg_index=0;
    if (furniture_index>0){
    while(slider_action<slider_reverse_elements){
        get_previous_pegs('canvas');
        slider_action++;
        }
    slider_action=0;}
    if (furniture_index%3 ==0 && furniture_index!=0){
        //click on the next button in the slider
        select_element("slider-top-right-button");
    }
    select_element("furniture-position-"+((furniture_index%3)+1));
    furniture_index++;
    if( furniture_index < furnitures.length ){

            setTimeout( peg_selection_loop, 500 );

    }
}


function peg_selection_loop(){
     if (peg_index%8 ==0 && peg_index!=0 && peg_index/8 != pegs.length/8){
        //click on the next button in the slider
        select_element("slider-bottom-right-button");
    }
    select_element("peg-position-"+((peg_index%8)+1));
    peg_index++;
    console.log('-================ peg index : '+peg_index);
    if( peg_index < pegs.length ){

    if (peg_index%8 ==0 && peg_index!=0){
            //click on the next button in the slider
            setTimeout( peg_selection_loop, 500 );
        }
        else{
        setTimeout( peg_selection_loop, 500 );
    }
    }
    if (peg_index == pegs.length && furniture_index!=furnitures.length){
        setTimeout( furniture_selection_loop, 500 );
    }

}
//window.onload = furniture_selection_loop();


