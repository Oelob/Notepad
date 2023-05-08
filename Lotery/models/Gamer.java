package models;


public class Gamer {
    
   protected int id;
   protected String name;

   public Gamer(int id, String name) {
        this.id = id;
        this.name = name;

   }

   public int getId() {
       return id;
   }
   public String getName() {
       return name;
   }
   @Override
   public String toString() {
       return String.format("ID игрока - %d\nИмя игрока - %s", this.id, this.name);
   }


}
