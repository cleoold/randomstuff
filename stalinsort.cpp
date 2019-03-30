#include <iostream>


// stalin_sort(array, len) sorts the array of integers in increasing order stalinly!
// ie if it encounters any element that is not in the right order, it will eliminate
// that inconsistency no problem. :->
// where [array] is the array to sort, [len] is its length.
// right. it is O(n^2) but that's because I moved elements after the inconsistency 
// forward by one. if I don't do this there'll be gaps that no comrade will fill in.
void stalin_sort(int *array, const int len) {
    int newlen = len;
    int last = *array;
    for (int *j = array+1; j < array+newlen;) {
        if (last <= *j) last = *(j++);
         else {
            *j = 0;
            for (int *k = j; k < array+newlen; ++k) *k = *(k+1);
            --newlen; // selectively delete
         }
    }
}

// prints array with [array] and length [len]
void print_array(int *array, int len) {
  for (int *j = array; j < array+len; ++j) {
    std::cout << *j;
    if (j < array+len-1) std::cout << " ";
  }
  std::cout << std::endl;
}


int main(void) {
    // sample output
    // -5 -2 -6 -7 0 1 3 3 4 5 6 4 3 1
    // -5 -2 0 1 3 3 4 5 6 0 0 0 0 0
    /*
    int a[14] = {-5,-2,-6,-7,0,1,3,3,4,5,6,4,3,1};
    print_array(a,14);
    stalin_sort(a,14);
    print_array(a,14);
    */
}
