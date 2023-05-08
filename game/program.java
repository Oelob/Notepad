package Game;

import Game.models.LoteryBox;
import Game.models.Toys;

public class program{
    public static void main(String[] args) {

        Toys toy = new Toys(1, "tiger", 5, 80, "fluffy");
        Toys toy2 = new Toys(2, "lion", 4, 60, "fluffy");
        Toys toy3 = new Toys(3, "cat", 3, 50, "plastic");
        

       

        LoteryBox<Toys> box = new LoteryBox<>();
        box.add(toy);
        box.add(toy2);
        box.add(toy3);
        box.printBox(box);

        
        
        

        
               

    }
}
