import models.Gamer;
import models.LoteryBox;
import models.Toys;

public class program{
    public static void main(String[] args) {

        Toys toy = new Toys(1, "tiger", 5, 80, "fluffy");
        Toys toy2 = new Toys(2, "lion", 4, 60, "fluffy");
        Toys toy3 = new Toys(3, "cat", 3, 50, "plastic");
        Toys toy4 = new Toys(4, "bycicle", 1, 20, "transport");
        Gamer gamer1 = new Gamer(1, "Ivan");
        Gamer gamer2 = new Gamer(2, "David");

       

        LoteryBox<Toys> box = new LoteryBox<>();
        box.add(toy);
        box.add(toy2);
        box.add(toy3);
        box.add(toy4);
        box.printBox(box);

        
        
        

        
               

    }
}
