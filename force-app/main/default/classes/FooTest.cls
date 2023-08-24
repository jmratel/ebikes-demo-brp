@IsTest
private class FooTest{
	@IsTest
	static void isTrue(){
		Foo f = new Foo();
		Assert.areEqual(true, f.getTrue());
	}
}