package Game.models;

public class Toys{

    protected int id;
    protected String name;
    protected int count;
    protected double weigh;
    protected String toy_category;

    public Toys (int id, String name, int count, double weigh, String toy_category) {
        this.id = id;
        this.name = name; 
        this.count = count;
        this.weigh = weigh;
        this.toy_category = toy_category;
    }

    public String getName(){
        return this.name;
    }

    public int getId() {
        return this.id;
    }

    public int getCount() {
        return this.count;
    }

    public double getWeigh() {
        return this.weigh;
    }

    public String getToyCategory(){
        return this.toy_category;
    }
    public void setWeigh(double weigh) {
        this.weigh = weigh;
    }

    @Override
    public String toString() {
        return String.format("Игрушка:\n ID - %d\n Name - %s\n Count - %d\n Weigh - %.2f%%\n Toy category - %s", 
        this.id, this.name, this.count, this.weigh, this.toy_category);
    }

}