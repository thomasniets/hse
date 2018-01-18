using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace сlasssss
{
    class Person
    {
        private string name;
        private uint age;
        private string phoneNumber;
        private string email;

        public string Name { get { return name; } set { name = value; } }
        public uint Age { get { return age; } set { age = value; } }
        public string PhoneNumber { get { return phoneNumber; } set { phoneNumber = value; } }
        public string Email { get { return email; } set { email = value; } }

        public Person()
        {

        }

        public Person(string name, uint age)
        {
            this.name = name;
            this.age = age;
        }

        public Person (string name, uint age, string phoneNumber, string email)
        {
            this.name = name;
            this.age = age;
            this.phoneNumber = phoneNumber;
            this.email = email;
        }

        public void personInfo()
        {
            Console.WriteLine("{0,1}, возраст: {1,2}, номер: {2,10}, мыло: {3,10}",name,age,phoneNumber,email);
        }
    }
}
