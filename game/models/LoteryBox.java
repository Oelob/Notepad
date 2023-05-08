
package Game.models;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class LoteryBox<Toys> implements Iterable<Toys>{

   private List<Toys> LotteryBox = new ArrayList<>();

   public void add(Toys el){
        LotteryBox.add(el);
    }

   public void remove(Toys el){
        LotteryBox.remove(el);
    }

    public void printBox(LoteryBox<Toys> arr){
        for (Toys toys : arr) {
            System.out.println(toys);
            System.out.println("===============");
        }
    }

    
  

    @Override
    public Iterator <Toys>iterator() {
        return new CustomIterator<Toys>(LotteryBox);
      
    }

    public class CustomIterator<T> implements Iterator<T>{
        int current_pos = 0; 
        List<T> temp_list;

        public CustomIterator(List<T> temp_list) {
            this.temp_list = temp_list;

        }
        @Override
        public boolean hasNext() {
            if (temp_list.size() >= current_pos+1){
                return true;
            }
            return false;
        }
        
        @Override
        public T next() {
            T value = temp_list.get(current_pos);
            current_pos++;
            return value;
        }
    }
}
