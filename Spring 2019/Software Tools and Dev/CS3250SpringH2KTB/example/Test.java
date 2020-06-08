class Test {

	static void main(String[] args) {
		System.out.println("Test!");
	}

	static int return0() {
		return 0;
	}

	static int return42() {
		return 42;
	}

	static int iadd(int a, int b) {
		return a + b;
	}

	static int isub(int a, int b) {
		return a - b;
	}

	static int imul(int a, int b) {
		return a * b;
	}

	static int print5() {
		System.out.println(5);
		return 0;
	}

	static int iconst_m1(){
		return -1;
	}

	static int iconst_1(){
		return 1;
	}

	static int iconst_2(){
		return 2;
	}

	static int iconst_3(){
		return 3;
	}

	static int iconst_4(){
		return 4;
	}

	static String astore_aload_0(){
		String stringOne = "hi";
		String stringTwo = "bye";
		String stringThree = "NO!";
		String stringFour = "YES!";
		return stringOne;

	}

	static String astore_aload_1(){
		String stringOne = "hi";
		String stringTwo = "bye";
		String stringThree = "NO!";
		String stringFour = "YES!";
		return stringTwo;

	}

	static String astore_aload_2(){
		String stringOne = "hi";
		String stringTwo = "bye";
		String stringThree = "NO!";
		String stringFour = "YES!";
		return stringThree;

	}

	static String astore_aload_3(){
		String stringOne = "hi";
		String stringTwo = "bye";
		String stringThree = "NO!";
		String stringFour = "YES!";
		return stringFour;

	}

	static int istore() {
		int one = 5;
		int two = 6;
		int three = 7;
		int four = 8;
		int five = 9;
		return two;
	}

	static int iload() {
		int one = 3;
		int two = 20;
		int three = 3;
		int four = 4;
		int five = 5;
		return five + four + three + two + one;
	}

	static long i2l() {
		int i = 20;
		long l = i;
		return l;
	}

	static char i2c() {
		int i = 97;
		char l = (char)i;
		return l;
	}

	static short i2s() {
		int i = 10;
		short l = (short)i;
		return l;
	}

	static byte i2b() {
		int i = 4;
		byte l = (byte)i;
		return l;
  }

	static long lstore() {
		long one = 1;
		long two = 1;
		long three = 1;
		long four = 1;
		long five = 1;
		return five;
	}

	static float i2f() {
		int i = 20;
		float f = i;
		return f;
	}

   static int intLdc() {
      int i = 120010;
      return i-10;
   }

   static double dconst_0() {
      return 0;
   }

   static double dconst_1() {
      return 1;
   }
	 static float fstore_fload_0() {
	    float floatOne = (float)0.0;
 		  float floatTwo = (float)1.0;
 		return floatOne;
	}
	static float fstore_fload_1() {
	    float floatOne = (float)0.0;
	    float floatTwo = (float)1.0;
	    float floatThree = (float)2.0;
	    float floatFour = (float)3.0;
	 return floatTwo;
 }
 static float fstore_fload_2() {
	   float floatOne = (float)0.0;
	   float floatTwo = (float)1.0;
	   float floatThree = (float)2.0;
	   float floatFour = (float)3.0;
	return floatThree;
}
static float fstore_fload_3() {
    float floatOne = (float)0.0;
    float floatTwo = (float)1.0;
    float floatThree = (float)2.0;
    float floatFour = (float)3.0;
 return floatFour;
}
static double f2d(){
	float a = (float)10.0;
	double c = a;
	return c;
}
static int f2i(){
	float a = (float)10.0;
	int d = (int) a;
	return d;
}
static long f2l(){
	float a = (float)10.0;
	long e = (long) a;
	return e;
}
static float fadd(){
	float a = (float)10.0;
	float b = (float)5.0;
	float f = a + b;
	return f;
}
static float fdiv(){
	float a = (float)10.0;
	float b = (float)5.0;
	float f = a / b;
	return f;
}
static float fmul(){
	float a = (float)10.0;
	float b = (float)5.0;
	float f = a * b;
	return f;
}
static float frem(){
	float a = (float)10.0;
	float b = (float)7.0;
	float f = a % b;
	return f;
}
static float fsub(){
	float a = (float)10.0;
	float b = (float)5.0;
	float f = a - b;
	return f;
}
static float fneg(){
    float a = (float)10.0;
	return -a;
}
 static float fReturn(){
	 return (float)0;
 }
static long lReturn(){
	return (long)0;
}
static long lstore_lload_0() {
	 long longOne = (long)0.0;
	 long longTwo = (long)1.0;
 return longOne;
}
static long lstore_lload_1() {
	 long longOne = (long)0.0;
	 long longTwo = (long)1.0;
	 long longThree = (long)2.0;
	 long longFour = (long)3.0;
return longTwo;
}
static long lstore_lload_2() {
	long longOne = (long)0.0;
	long longTwo = (long)1.0;
	long longThree = (long)2.0;
	long longFour = (long)3.0;
return longThree;
}
static long lstore_lload_3() {
 long longOne = (long)0.0;
 long longTwo = (long)1.0;
 long longThree = (long)2.0;
 long longFour = (long)3.0;
return longFour;
}
static double l2d(){
long a = (long)10.0;
double c = a;
return c;
}
static int l2i(){
long a = (long)10.0;
int d = (int) a;
return d;
}
static float l2f(){
long a = (long)10.0;
float e = (float) a;
return e;
}
static long ladd(){
long a = (long)10.0;
long b = (long)5.0;
long f = a + b;
return f;
}
static long ldiv(){
long a = (long)10.0;
long b = (long)5.0;
long f = a / b;
return f;
}
static long lmul(){
long a = (long)10.0;
long b = (long)5.0;
long f = a * b;
return f;
}
static long lrem(){
long a = (long)10.0;
long b = (long)7.0;
long f = a % b;
return f;
}
static long lsub(){
long a = (long)10.0;
long b = (long)5.0;
long f = a - b;
return f;
}
static long lneg(long a){
	a = -a;
	return a;
}
static long land(){
long a = (long)10.0;
long b = (long)15.0;
long f = a & b;
return f;
}
static long lor(long a, long b){
long f = a | b;
return f;
}
static long lxor(){
long a = (long)10.0;
long b = (long)15.0;
long f = a ^ b;
return f;
}
static long lshl(){
long a = (long)10.0;
long b = (int)15;
long f = a << b;
return f;
}
static long lshr(){
long a = (long)15.0;
long b = (int)1;
long f = a >> b;
return f;
}

}
