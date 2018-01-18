using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace сlasssss
{
    class Program
    {
        static void Main(string[] args)
        {
            //Person p1 = new Person("Boris", 55);
            //p1.personInfo();

            //Person p2 = new Person
            //{
            //    Name = "Dmitry",
            //    Age = 33,
            //    PhoneNumber = "+79777777777",
            //    Email = "vava@hse.ru"

            //};

            //p2.personInfo();

            //Person p3 = new Person("Serge", 45, "+79777777777", "durak@mail.ru");
            //p3.personInfo();

            //DateTime d = new DateTime();

            //var d1 = DateTime.Now.Year;
            //Console.WriteLine(d1);

            //var d2 = DateTime.Now.DayOfWeek;
            //Console.WriteLine(d2);

            PersonBirthDate pn = new PersonBirthDate
            {
                Name = "Serge",
                BirthDate = new DateTime(1987, 8, 24)
            };


            Console.WriteLine(pn.Info);
            Console.ReadLine();
        }
    }
}
