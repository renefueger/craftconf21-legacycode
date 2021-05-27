using System;
using NUnit.Framework;

namespace tests
{
    [TestFixture]
    public class LegacyTests
    {
        [Test]
        public void AFailingUnitTest()
        {
            Assert.Fail("it is failing for the correct reasons");
        }
    }
}