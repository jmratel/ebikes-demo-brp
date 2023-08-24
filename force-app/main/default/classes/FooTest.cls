@IsTest
private class FooTest{
	@IsTest
	static void isTrue(){
		///////////////
		Assert.areEqual(false, Foo.getTrue());
	}
}