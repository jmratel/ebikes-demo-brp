@IsTest
private class FooTest{
	@IsTest
	static void isTrue(){
		///////////////
		Assert.areEqual(true, Foo.getTrue());
	}
}