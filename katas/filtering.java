import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class filtering {
    public static void main(String[] args) {
        int[] a = { 1, 2, -3, 4, -5 };
        int[] b = Arrays.stream(a).filter(x -> x > 0).toArray();

        List<Integer> c = Arrays.asList(1, 2, -3, 4, -5);
        List<Integer> d = c.stream().filter(x -> x > 0).collect(Collectors.toList());

        System.out.println(Arrays.toString(b));
        System.out.println(d);
    }
}