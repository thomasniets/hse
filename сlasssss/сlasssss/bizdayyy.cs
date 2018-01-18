using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace сlasssss
{
    class PersonBirthDate
    {
        private string name;
        private DateTime birthDate;

        public string Name { get { return name; } set { name = value; } }
        public DateTime BirthDate { get { return birthDate; } set { birthDate = value; } }

        public int getAge()
        {
            var currentDate = DateTime.Now;
            int age = currentDate.Year - birthDate.Year;
            return age;
        }

        public string Info
        {
            get { return $"{Name} is { getAge()} years old"; }
        }
    }
}
